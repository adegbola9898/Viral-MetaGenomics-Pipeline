#!/usr/bin/env python

from pathlib import Path
import sys
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq


def get_qualifier(feature, key):
    return feature.qualifiers.get(key, [""])[0]


def feature_name(feature):
    gene = get_qualifier(feature, "gene")
    product = get_qualifier(feature, "product")
    note = get_qualifier(feature, "note")

    if gene and product:
        return gene, product
    if gene:
        return gene, gene
    if product:
        return "", product
    if note:
        return "", note[:80]
    return "", "unnamed_CDS"


def feature_positions(feature):
    """
    Return genomic positions covered by feature in coding order.
    Positions are 0-based.
    """
    positions = []

    for part in feature.location.parts if hasattr(feature.location, "parts") else [feature.location]:
        positions.extend(range(int(part.start), int(part.end)))

    if feature.location.strand == -1:
        positions = list(reversed(positions))

    return positions


def annotate_snv(row, record, cds_features):
    pos1 = int(row["position"])
    pos0 = pos1 - 1
    ref_base = str(row["ref"]).upper()
    alt_base = str(row["alt"]).upper()

    if len(ref_base) != 1 or len(alt_base) != 1:
        return {
            "effect": "not_snv",
            "codon_position": "",
            "ref_codon": "",
            "alt_codon": "",
            "ref_aa": "",
            "alt_aa": "",
            "aa_position": "",
        }

    hits = []

    for feature in cds_features:
        positions = feature_positions(feature)

        if pos0 not in positions:
            continue

        idx = positions.index(pos0)
        codon_start_idx = (idx // 3) * 3
        codon_positions = positions[codon_start_idx:codon_start_idx + 3]

        if len(codon_positions) != 3:
            continue

        ref_seq = record.seq
        ref_codon_list = [str(ref_seq[p]).upper() for p in codon_positions]

        alt_codon_list = ref_codon_list.copy()
        base_index_in_codon = idx % 3

        # If CDS is on reverse strand, alt base must be reverse complemented
        if feature.location.strand == -1:
            alt_for_codon = str(Seq(alt_base).reverse_complement())
        else:
            alt_for_codon = alt_base

        alt_codon_list[base_index_in_codon] = alt_for_codon

        ref_codon = "".join(ref_codon_list)
        alt_codon = "".join(alt_codon_list)

        ref_aa = str(Seq(ref_codon).translate())
        alt_aa = str(Seq(alt_codon).translate())

        if ref_aa == alt_aa:
            effect = "synonymous"
        elif alt_aa == "*":
            effect = "nonsense"
        elif ref_aa == "*":
            effect = "stop_lost"
        else:
            effect = "missense"

        gene, product = feature_name(feature)

        hits.append({
            "effect": effect,
            "codon_position": base_index_in_codon + 1,
            "ref_codon": ref_codon,
            "alt_codon": alt_codon,
            "ref_aa": ref_aa,
            "alt_aa": alt_aa,
            "aa_position": (idx // 3) + 1,
            "effect_gene": gene,
            "effect_product": product,
        })

    if not hits:
        return {
            "effect": "noncoding_or_unannotated",
            "codon_position": "",
            "ref_codon": "",
            "alt_codon": "",
            "ref_aa": "",
            "alt_aa": "",
            "aa_position": "",
            "effect_gene": "",
            "effect_product": "",
        }

    # If overlapping CDS, join effects
    keys = hits[0].keys()
    return {k: ";".join(str(h[k]) for h in hits) for k in keys}


def main():
    if len(sys.argv) != 4:
        print("Usage: annotate_snv_effects.py <annotated_variants.tsv> <reference.gb> <output.tsv>")
        sys.exit(1)

    variants_path = Path(sys.argv[1])
    genbank_path = Path(sys.argv[2])
    out_path = Path(sys.argv[3])

    record = SeqIO.read(genbank_path, "genbank")
    cds_features = [f for f in record.features if f.type == "CDS"]

    df = pd.read_csv(variants_path, sep="\t")

    effects = []
    for _, row in df.iterrows():
        effects.append(annotate_snv(row, record, cds_features))

    effect_df = pd.DataFrame(effects)
    out = pd.concat([df, effect_df], axis=1)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, sep="\t", index=False)

    print(f"Wrote: {out_path}")
    print(out["effect"].value_counts())


if __name__ == "__main__":
    main()

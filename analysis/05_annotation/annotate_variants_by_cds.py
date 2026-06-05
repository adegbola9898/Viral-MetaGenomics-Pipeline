#!/usr/bin/env python

from pathlib import Path
import sys
import pandas as pd
from Bio import SeqIO


def feature_label(feature):
    q = feature.qualifiers

    gene = q.get("gene", [""])[0]
    product = q.get("product", [""])[0]
    note = q.get("note", [""])[0]

    if gene and product:
        return gene, product
    if gene:
        return gene, gene
    if product:
        return "", product
    if note:
        return "", note[:80]
    return "", "unnamed_CDS"


def pos_in_feature(pos_1based, feature):
    pos0 = pos_1based - 1
    return pos0 in feature.location


def load_cds_features(genbank_file):
    record = SeqIO.read(genbank_file, "genbank")
    features = []

    for feature in record.features:
        if feature.type != "CDS":
            continue

        gene, product = feature_label(feature)

        features.append(
            {
                "start": int(feature.location.start) + 1,
                "end": int(feature.location.end),
                "strand": feature.location.strand,
                "gene": gene,
                "product": product,
                "location": str(feature.location),
                "feature": feature,
            }
        )

    return features


def annotate_variant(pos, cds_features):
    hits = []

    for f in cds_features:
        if pos_in_feature(pos, f["feature"]):
            hits.append(f)

    if not hits:
        return {
            "region_type": "noncoding",
            "gene": "",
            "product": "",
            "feature_location": "",
            "strand": "",
        }

    # If overlapping CDS, join labels
    genes = ";".join([h["gene"] for h in hits if h["gene"]])
    products = ";".join([h["product"] for h in hits if h["product"]])
    locations = ";".join([h["location"] for h in hits])
    strands = ";".join([str(h["strand"]) for h in hits])

    return {
        "region_type": "CDS",
        "gene": genes,
        "product": products,
        "feature_location": locations,
        "strand": strands,
    }


def main():
    if len(sys.argv) != 4:
        print("Usage: annotate_variants_by_cds.py <variants.tsv> <reference.gb> <output.tsv>")
        sys.exit(1)

    variants_file = Path(sys.argv[1])
    genbank_file = Path(sys.argv[2])
    output_file = Path(sys.argv[3])

    cds_features = load_cds_features(genbank_file)
    df = pd.read_csv(variants_file, sep="\t")

    annotations = []
    for _, row in df.iterrows():
        annotations.append(annotate_variant(int(row["position"]), cds_features))

    ann = pd.DataFrame(annotations)
    out = pd.concat([df, ann], axis=1)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(output_file, sep="\t", index=False)

    print(f"Wrote annotated variants: {output_file}")
    print(out["region_type"].value_counts())


if __name__ == "__main__":
    main()

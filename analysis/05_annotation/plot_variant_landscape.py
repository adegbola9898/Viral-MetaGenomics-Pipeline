#!/usr/bin/env python

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from Bio import SeqIO

CONFIGS = [
    {
        "sample": "AIAMA_GOT005_OS_S43",
        "title": "Variant landscape — Goat AdV-12-like genome",
        "variants": "results/tables/variants/high_confidence/AIAMA_GOT005_OS_S43.X73487.1.high_confidence_coding_snvs.tsv",
        "genbank": "refs/annotations/X73487.gb",
        "out_prefix": "results/figures/AIAMA_GOT005_OS_S43_variant_landscape",
    },
    {
        "sample": "AINWZDOG001_S37",
        "title": "Variant landscape — Dog AdV-18-like genome",
        "variants": "results/tables/variants/high_confidence/AINWZDOG001_S37.GU191019.1.high_confidence_coding_snvs.tsv",
        "genbank": "refs/annotations/GU191019.gb",
        "out_prefix": "results/figures/AINWZDOG001_S37_variant_landscape",
    },
]

KEY_PRODUCTS = [
    "E1A",
    "E1B",
    "DNA polymerase",
    "DNA binding",
    "terminal protein",
    "52",
    "protein IIIa",
    "penton",
    "protein V",
    "protein VI",
    "hexon",
    "100",
    "fiber",
    "E4",
]


def clean_label(gene, product):
    text = f"{gene} {product}".strip()

    for key in KEY_PRODUCTS:
        if key.lower() in text.lower():
            return key

    if product:
        return product[:18]
    if gene:
        return gene[:18]
    return "CDS"


def extract_cds(genbank_path):
    record = SeqIO.read(genbank_path, "genbank")
    cds_rows = []

    for feature in record.features:
        if feature.type != "CDS":
            continue

        q = feature.qualifiers
        gene = q.get("gene", [""])[0]
        product = q.get("product", [""])[0]
        note = q.get("note", [""])[0]

        if not product and note:
            product = note[:40]

        label = clean_label(gene, product)

        cds_rows.append(
            {
                "start": int(feature.location.start) + 1,
                "end": int(feature.location.end),
                "strand": feature.location.strand,
                "label": label,
            }
        )

    return record, pd.DataFrame(cds_rows)


def simplify_effect(effect):
    effect = str(effect)
    if "missense" in effect and "synonymous" in effect:
        return "mixed"
    if "missense" in effect:
        return "missense"
    if "synonymous" in effect:
        return "synonymous"
    return "other"


def plot_landscape(config):
    Path("results/figures").mkdir(parents=True, exist_ok=True)

    record, cds = extract_cds(config["genbank"])
    genome_len = len(record.seq)

    variants = pd.read_csv(config["variants"], sep="\t")
    variants["effect_simple"] = variants["effect"].apply(simplify_effect)

    y_map = {
        "synonymous": 2,
        "missense": 3,
        "mixed": 4,
        "other": 1,
    }

    variants["y"] = variants["effect_simple"].map(y_map).fillna(1)

    fig, ax = plt.subplots(figsize=(14, 5))

    for effect in ["synonymous", "missense", "mixed", "other"]:
        sub = variants[variants["effect_simple"] == effect]
        if sub.empty:
            continue
        ax.scatter(
            sub["position"],
            sub["y"],
            label=effect,
            s=18,
            alpha=0.8,
        )

    gene_y = 0.35

    for _, row in cds.iterrows():
        ax.plot(
            [row["start"], row["end"]],
            [gene_y, gene_y],
            linewidth=6,
            solid_capstyle="butt",
        )

        mid = (row["start"] + row["end"]) / 2
        ax.text(
            mid,
            gene_y - 0.18,
            row["label"],
            ha="center",
            va="top",
            fontsize=7,
            rotation=45,
        )

    ax.set_xlim(1, genome_len)
    ax.set_ylim(0, 4.5)

    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(["other", "synonymous", "missense", "mixed"])

    ax.set_xlabel("Genome position (bp)")
    ax.set_ylabel("Variant consequence")
    ax.set_title(config["title"])
    ax.legend(title="Effect", loc="upper right")

    plt.tight_layout()

    png = config["out_prefix"] + ".png"
    pdf = config["out_prefix"] + ".pdf"

    plt.savefig(png, dpi=300, bbox_inches="tight")
    plt.savefig(pdf, bbox_inches="tight")
    plt.close()

    print(f"Wrote {png}")
    print(f"Wrote {pdf}")


def main():
    for config in CONFIGS:
        plot_landscape(config)


if __name__ == "__main__":
    main()

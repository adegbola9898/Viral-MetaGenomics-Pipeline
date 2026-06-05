#!/usr/bin/env python

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

FILES = [
    {
        "path": "results/tables/variants/AIAMA_GOT005_OS_S43.X73487.1.annotated_variants.tsv",
        "sample": "AIAMA_GOT005_OS_S43",
        "title": "Variant burden by product — Goat AdV-12-like genome",
        "out": "results/figures/AIAMA_GOT005_OS_S43_variant_burden.png",
    },
    {
        "path": "results/tables/variants/AINWZDOG001_S37.GU191019.1.annotated_variants.tsv",
        "sample": "AINWZDOG001_S37",
        "title": "Variant burden by product — Dog AdV-18-like genome",
        "out": "results/figures/AINWZDOG001_S37_variant_burden.png",
    },
]

Path("results/figures").mkdir(parents=True, exist_ok=True)

for item in FILES:
    df = pd.read_csv(item["path"], sep="\t")

    cds = df[df["region_type"] == "CDS"].copy()
    cds["product"] = cds["product"].fillna("unknown_product")
    cds.loc[cds["product"].str.strip() == "", "product"] = "unknown_product"

    counts = (
        cds["product"]
        .value_counts()
        .head(15)
        .sort_values(ascending=True)
    )

    fig, ax = plt.subplots(figsize=(10, 7))
    counts.plot(kind="barh", ax=ax)

    ax.set_xlabel("Number of variants")
    ax.set_ylabel("Gene / product")
    ax.set_title(item["title"])

    plt.tight_layout()
    plt.savefig(item["out"], dpi=300, bbox_inches="tight")
    plt.savefig(item["out"].replace(".png", ".pdf"), bbox_inches="tight")
    plt.close()

    print(f"Wrote {item['out']}")

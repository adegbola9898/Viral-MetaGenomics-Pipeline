#!/usr/bin/env python

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

FILES = [
    {
        "path": "results/tables/variants/high_confidence/AIAMA_GOT005_OS_S43.X73487.1.high_confidence_coding_snvs.tsv",
        "title": "Goat AdV-12-like genome",
        "prefix": "AIAMA_GOT005_OS_S43"
    },
    {
        "path": "results/tables/variants/high_confidence/AINWZDOG001_S37.GU191019.1.high_confidence_coding_snvs.tsv",
        "title": "Dog AdV-18-like genome",
        "prefix": "AINWZDOG001_S37"
    }
]

outdir = Path("results/figures")
outdir.mkdir(parents=True, exist_ok=True)

for item in FILES:

    df = pd.read_csv(item["path"], sep="\t")

    df = df[
        df["effect"].isin([
            "synonymous",
            "missense"
        ])
    ]

    counts = (
        df.groupby(["product", "effect"])
        .size()
        .unstack(fill_value=0)
    )

    counts["total"] = counts.sum(axis=1)

    counts = (
        counts
        .sort_values("total", ascending=False)
        .head(15)
        .drop(columns=["total"])
    )

    fig, ax = plt.subplots(figsize=(10, 6))

    counts.plot(
        kind="bar",
        stacked=True,
        ax=ax
    )

    ax.set_title(
        f"Missense vs synonymous variants by gene\n{item['title']}"
    )

    ax.set_xlabel("Gene / protein")
    ax.set_ylabel("Number of variants")

    plt.xticks(
        rotation=70,
        ha="right"
    )

    plt.tight_layout()

    png = outdir / f"{item['prefix']}_missense_vs_synonymous.png"
    pdf = outdir / f"{item['prefix']}_missense_vs_synonymous.pdf"

    plt.savefig(png, dpi=300, bbox_inches="tight")
    plt.savefig(pdf, bbox_inches="tight")
    plt.close()

    print("Wrote", png)

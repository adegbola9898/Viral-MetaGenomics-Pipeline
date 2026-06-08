#!/usr/bin/env python

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

CONFIGS = [
    {
        "path": "results/intermediate/coverage/AIAMA_GOT005_OS_S43.X73487.1.depth.tsv",
        "title": "Coverage profile — Goat AdV-12-like genome",
        "out_prefix": "results/figures/AIAMA_GOT005_OS_S43_coverage_profile_capped",
    },
    {
        "path": "results/intermediate/coverage/AINWZDOG001_S37.GU191019.1.depth.tsv",
        "title": "Coverage profile — Dog AdV-18-like genome",
        "out_prefix": "results/figures/AINWZDOG001_S37_coverage_profile_capped",
    },
]

Path("results/figures").mkdir(parents=True, exist_ok=True)

for config in CONFIGS:
    df = pd.read_csv(
        config["path"],
        sep="\t",
        header=None,
        names=["reference", "position", "depth"]
    )

    mean_depth = df["depth"].mean()
    breadth = (df["depth"] > 0).mean() * 100
    max_depth = df["depth"].max()
    max_pos = df.loc[df["depth"].idxmax(), "position"]

    cap = df["depth"].quantile(0.99)
    df["depth_capped"] = df["depth"].clip(upper=cap)

    fig, ax = plt.subplots(figsize=(14, 4))
    ax.plot(df["position"], df["depth_capped"], linewidth=0.6)

    ax.set_title(config["title"])
    ax.set_xlabel("Genome position (bp)")
    ax.set_ylabel(f"Read depth capped at 99th percentile ({cap:.0f}×)")

    ax.text(
        0.01,
        0.95,
        f"Mean depth: {mean_depth:.2f}×\n"
        f"Breadth: {breadth:.2f}%\n"
        f"Max depth: {max_depth:.0f}× at {max_pos} bp",
        transform=ax.transAxes,
        va="top",
        ha="left",
        bbox=dict(boxstyle="round", alpha=0.2)
    )

    plt.tight_layout()

    png = config["out_prefix"] + ".png"
    pdf = config["out_prefix"] + ".pdf"

    plt.savefig(png, dpi=300, bbox_inches="tight")
    plt.savefig(pdf, bbox_inches="tight")
    plt.close()

    print(f"Wrote {png}")
    print(f"Wrote {pdf}")

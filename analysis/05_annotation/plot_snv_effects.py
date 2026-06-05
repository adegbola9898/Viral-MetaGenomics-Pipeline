#!/usr/bin/env python

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

FILES = [
    {
        "path": "results/tables/variants/AIAMA_GOT005_OS_S43.X73487.1.snv_effects.tsv",
        "title": "SNV consequences — Goat AdV-12-like genome",
        "out": "results/figures/AIAMA_GOT005_OS_S43_snv_effects.png",
    },
    {
        "path": "results/tables/variants/AINWZDOG001_S37.GU191019.1.snv_effects.tsv",
        "title": "SNV consequences — Dog AdV-18-like genome",
        "out": "results/figures/AINWZDOG001_S37_snv_effects.png",
    },
]

Path("results/figures").mkdir(parents=True, exist_ok=True)

def simplify_effect(effect):
    effect = str(effect)
    if "missense" in effect and "synonymous" in effect:
        return "mixed_overlap"
    if "missense" in effect:
        return "missense"
    if "synonymous" in effect:
        return "synonymous"
    if "nonsense" in effect:
        return "nonsense"
    if "stop_lost" in effect:
        return "stop_lost"
    if "not_snv" in effect:
        return "not_snv"
    if "noncoding" in effect:
        return "noncoding"
    return effect

for item in FILES:
    df = pd.read_csv(item["path"], sep="\t")
    df["effect_simple"] = df["effect"].apply(simplify_effect)

    counts = df["effect_simple"].value_counts().sort_values(ascending=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    counts.plot(kind="barh", ax=ax)

    ax.set_xlabel("Number of variants")
    ax.set_ylabel("Predicted consequence")
    ax.set_title(item["title"])

    plt.tight_layout()
    plt.savefig(item["out"], dpi=300, bbox_inches="tight")
    plt.savefig(item["out"].replace(".png", ".pdf"), bbox_inches="tight")
    plt.close()

    print(f"Wrote {item['out']}")

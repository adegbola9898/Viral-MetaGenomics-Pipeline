#!/usr/bin/env python

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

infile = "results/tables/variants/adenovirus_variant_allele_frequencies.tsv"

df = pd.read_csv(infile, sep="\t")

groups = [
    df.loc[df["genome"] == "Goat AdV-12-like", "af"],
    df.loc[df["genome"] == "Dog AdV-18-like", "af"],
]

fig, ax = plt.subplots(figsize=(7, 5))

ax.boxplot(
    groups,
    labels=["Goat\nAdV-12-like", "Dog\nAdV-18-like"],
    showfliers=True
)

ax.set_ylabel("Variant allele frequency")
ax.set_ylim(0, 1.05)
ax.set_title("Variant allele frequency distribution")

plt.tight_layout()

outdir = Path("results/figures")
outdir.mkdir(parents=True, exist_ok=True)

png = outdir / "adenovirus_variant_allele_frequency_boxplot.png"
pdf = outdir / "adenovirus_variant_allele_frequency_boxplot.pdf"

plt.savefig(png, dpi=300, bbox_inches="tight")
plt.savefig(pdf, bbox_inches="tight")

print(f"Wrote {png}")
print(f"Wrote {pdf}")

#!/usr/bin/env python

from pathlib import Path
import subprocess
import pandas as pd

CONFIGS = [
    {
        "sample": "AIAMA_GOT005_OS_S43",
        "genome": "Goat AdV-12-like",
        "vcf": "results/intermediate/consensus/AIAMA_GOT005_OS_S43.X73487.1.vcf.gz",
    },
    {
        "sample": "AINWZDOG001_S37",
        "genome": "Dog AdV-18-like",
        "vcf": "results/intermediate/consensus/AINWZDOG001_S37.GU191019.1.vcf.gz",
    },
]

rows = []

for cfg in CONFIGS:
    cmd = [
        "bcftools", "query",
        "-f", "%CHROM\t%POS\t%REF\t%ALT[\t%DP\t%AD]\n",
        cfg["vcf"]
    ]

    output = subprocess.check_output(cmd, text=True)

    for line in output.strip().splitlines():
        chrom, pos, ref, alt, dp, ad = line.split("\t")[:6]

        ad_parts = ad.split(",")
        if len(ad_parts) < 2:
            continue

        try:
            ref_depth = int(ad_parts[0])
            alt_depth = max(int(x) for x in ad_parts[1:] if x != ".")
            total_depth = ref_depth + alt_depth
        except ValueError:
            continue

        if total_depth == 0:
            continue

        rows.append({
            "sample": cfg["sample"],
            "genome": cfg["genome"],
            "chrom": chrom,
            "position": int(pos),
            "ref": ref,
            "alt": alt,
            "dp": int(dp),
            "ref_depth": ref_depth,
            "alt_depth": alt_depth,
            "total_depth_ad": total_depth,
            "af": alt_depth / total_depth,
        })

df = pd.DataFrame(rows)

outdir = Path("results/tables/variants")
outdir.mkdir(parents=True, exist_ok=True)

out = outdir / "adenovirus_variant_allele_frequencies.tsv"
df.to_csv(out, sep="\t", index=False)

print(f"Wrote {out}")
print(df.groupby("genome")["af"].describe())

#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "Usage: $0 <sample_id> <reference_name> <vcf.gz>"
  exit 1
fi

SAMPLE="$1"
REF="$2"
VCF="$3"

OUTDIR="results/tables/variants"
mkdir -p "$OUTDIR"

OUT="$OUTDIR/${SAMPLE}.${REF}.variants.tsv"

echo -e "sample_id\treference\tposition\tref\talt\tqual\tdepth\tmapping_quality\tvariant_type" > "$OUT"

bcftools query \
  -f '%CHROM\t%POS\t%REF\t%ALT\t%QUAL\t%INFO/DP\t%INFO/MQ\n' \
  "$VCF" \
| awk -v sample="$SAMPLE" -v refname="$REF" 'BEGIN{OFS="\t"}{
    type="SNV";
    if (length($3) != length($4)) type="INDEL";
    print sample, refname, $2, $3, $4, $5, $6, $7, type
}' >> "$OUT"

echo "Variant table written to: $OUT"

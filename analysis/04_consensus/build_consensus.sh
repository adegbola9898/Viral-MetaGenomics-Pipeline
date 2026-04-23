#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "Usage: $0 <sample_id> <bam_file> <reference_name> [reference_fasta]"
  exit 1
fi

SAMPLE="$1"
BAM="$2"
REF_NAME="$3"
REF_FASTA="${4:-refs/adenovirus/adenovirus_panel.fasta}"

OUTDIR="results/intermediate/consensus"
mkdir -p "$OUTDIR"

TMP_REF="$OUTDIR/${REF_NAME}.ref.fa"
VCF="$OUTDIR/${SAMPLE}.${REF_NAME}.vcf.gz"
CONS="$OUTDIR/${SAMPLE}.${REF_NAME}.consensus.fasta"

echo "Building consensus for $SAMPLE against $REF_NAME"

# extract just the target reference sequence
samtools faidx "$REF_FASTA" "$REF_NAME" > "$TMP_REF"

# call variants on the target reference
bcftools mpileup -Ou -f "$REF_FASTA" -r "$REF_NAME" "$BAM" \
  | bcftools call --ploidy 1 -mv -Oz -o "$VCF"

bcftools index -f "$VCF"

# apply variants to the extracted target reference
bcftools consensus -f "$TMP_REF" "$VCF" > "$CONS"

echo "Consensus sequence written to:"
echo "$CONS"

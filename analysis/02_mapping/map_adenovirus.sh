#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "Usage: $0 <sample_id> <R1.fastq.gz> <R2.fastq.gz> [reference.fasta]"
  exit 1
fi

SAMPLE="$1"
R1="$2"
R2="$3"
REF="${4:-refs/adenovirus/adenovirus_panel.fasta}"

OUTDIR="results/intermediate/mapping"
TABLEDIR="results/tables"

mkdir -p "$OUTDIR" "$TABLEDIR"

echo "Running mapping for sample: $SAMPLE"
echo "Reference: $REF"
echo "R1: $R1"
echo "R2: $R2"

bwa mem -t 8 "$REF" "$R1" "$R2" \
  | samtools view -bS - \
  | samtools sort -o "$OUTDIR/${SAMPLE}.bam"

samtools index "$OUTDIR/${SAMPLE}.bam"

samtools flagstat "$OUTDIR/${SAMPLE}.bam" > "$TABLEDIR/${SAMPLE}.flagstat.txt"

echo "Done."
echo "BAM: $OUTDIR/${SAMPLE}.bam"
echo "Index: $OUTDIR/${SAMPLE}.bam.bai"
echo "Flagstat: $TABLEDIR/${SAMPLE}.flagstat.txt"

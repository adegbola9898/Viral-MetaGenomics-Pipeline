# Adenovirus Reference Panel

## Date
2026-04-23

## Accessions used
- X73487.1 (AdV-12)
- GU191019.1 (AdV-18)
- JN226752.1 (AdV-25)
- MG925783.1 (AdV-41)
- AC_000007.1 (AdV-2)

## Source
Downloaded from NCBI using efetch API.

## Processing steps
1. Individual FASTA files downloaded via efetch
2. Combined into a single panel:
   - adenovirus_panel.fasta
3. Headers cleaned using seqkit:
   - removed descriptive text after accession
4. Indexed using BWA:
   - bwa index adenovirus_panel.fasta

## Purpose
- Mapping validation
- Coverage analysis
- Initial classification

## Notes
- Panel intentionally small for fast validation
- Will expand later for phylogeny if needed

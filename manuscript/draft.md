## Adenovirus – Mapping Validation (AIAMA_GOT005_OS_S43)

Mapping of raw reads to the adenovirus reference panel yielded:

- Total reads: ~24.7 million
- Mapped reads: ~162,881 (~0.66%)
- Properly paired: ~0.65%

The mapping rate is consistent with expected viral signal in metagenomic data.

Importantly, a substantial number of reads mapped across the adenovirus panel, supporting the presence of adenovirus-like sequences in this sample.

Next steps:
- assess genome-wide coverage
- confirm whether signal spans the full genome or localized regions


### Adenovirus Coverage Analysis (AIAMA_GOT005_OS_S43)

Per-reference coverage analysis revealed a dominant signal corresponding to Human adenovirus type 12 (X73487.1).

- Coverage breadth: 96.5%
- Mean depth: ~47×
- Genome-wide distribution of coverage

Other adenovirus references showed substantially lower coverage breadth (<25%), with localized high-depth regions consistent with sequence similarity rather than independent viral signals.

These results support the presence of a near-complete AdV-12–like genome in this sample.


### Adenovirus Genome Reconstruction — AIAMA_GOT005_OS_S43

Mapping and coverage analysis identified a dominant adenovirus signal corresponding to reference X73487.1 (Human adenovirus type 12).

Per-reference coverage metrics were:
- Coverage breadth: 96.5%
- Mean depth: ~47×
- Genome-wide distribution of reads

Consensus genome reconstruction yielded a ~34 kb sequence with 486 variants relative to the reference.

BLAST analysis confirmed:
- Top hit: X73487.1
- Percent identity: 98.492%
- Alignment length: 34,155 bp

Other adenovirus references showed substantially lower coverage breadth (<25%) and fragmented alignments, consistent with cross-mapping due to sequence similarity rather than independent viral signals.

These results support the presence of a near-complete AdV-12–like genome in this sample.

### Adenovirus Genome Reconstruction — AINWZDOG001_S37

Mapping and coverage analysis identified a dominant adenovirus signal corresponding to reference GU191019.1 (Human adenovirus type 18).

Per-reference coverage metrics were:
- Coverage breadth: 98.06%
- Mean depth: ~39.5×
- Genome-wide distribution of reads

Consensus genome reconstruction yielded a ~34 kb sequence with 336 variants relative to the reference.

BLAST analysis confirmed:
- Top hit: GU191019.1
- Percent identity: 98.973%
- Alignment length: 34,177 bp

Other adenovirus references showed substantially lower coverage breadth (<25%) and fragmented alignments, consistent with cross-mapping due to sequence similarity rather than independent viral signals.

These results support the presence of a near-complete AdV-18–like genome in this sample.

### Adenovirus Mapping and Coverage — AINWZDOG002_S38

Mapping and per-reference coverage analysis identified the strongest signal against GU191019.1 (Human adenovirus type 18). However, coverage breadth was limited:

- Coverage breadth: 26.95%
- Mean depth: ~6.9×

All other adenovirus references showed even lower breadth (<5%). These results indicate a partial AdV-18–like signal, but do not support reconstruction of a near-complete genome for this sample.

Accordingly, this sample was retained as a lower-confidence adenovirus-positive sample and not advanced to full genome reconstruction at this stage.

### Adenovirus Mapping and Coverage — AIAMA_GOT007_OS_S45

Mapping and per-reference coverage analysis identified only weak partial adenovirus-like signal in this sample. The highest breadth of coverage was observed against MG925783.1, but remained limited:

- Coverage breadth: 11.99%
- Mean depth: ~7.3×

Other references showed similarly low breadth (<10–12%), indicating sparse and fragmented alignment rather than genome-wide support. These results do not support reconstruction of a near-complete adenovirus genome for this sample.

Accordingly, this sample was retained as a low-confidence adenovirus-positive sample and not advanced to consensus genome reconstruction or BLAST-based genome validation.

### Adenovirus Mapping — AIAMASHEEP002_S54

Read mapping identified only trace adenovirus-like signal in this sample. A total of 20 reads mapped to AC_000007.1, while all other adenovirus references had zero mapped reads.

This level of signal was considered below the threshold for meaningful validation. Accordingly, this sample was not advanced to per-reference coverage analysis, consensus genome reconstruction, or BLAST-based genome validation.

### Summary of Adenovirus Detection Across Samples

A total of five samples were evaluated for adenovirus presence and genome reconstruction.

- Two samples yielded near-complete genomes:
  - AIAMA_GOT005_OS_S43 (AdV-12–like)
  - AINWZDOG001_S37 (AdV-18–like)

- One sample showed partial adenovirus signal:
  - AINWZDOG002_S38 (partial AdV-18–like)

- Two samples showed weak or trace signal:
  - AIAMA_GOT007_OS_S45 (weak partial signal)
  - AIAMASHEEP002_S54 (trace signal; 20 reads only)

These results highlight substantial variability in adenovirus signal strength across samples. While some samples support full genome reconstruction and downstream phylogenetic analysis, others show only fragmented or minimal evidence of viral presence.

This distinction is critical for avoiding over-interpretation of low-abundance metagenomic detections.

### Phylogenetic Analysis of Reconstructed Adenovirus Genomes

Phylogenetic analysis was performed using maximum likelihood inference on an alignment of the reconstructed consensus genomes alongside representative adenovirus reference sequences.

The resulting tree topology showed:

- AIAMA_GOT005_OS_S43 clustered with X73487.1 (Human adenovirus type 12 lineage)
- AINWZDOG001_S37 clustered with GU191019.1 (Human adenovirus type 18 lineage)

Both placements were supported by strong bootstrap values (100), indicating high confidence in lineage assignment.

Other adenovirus references formed distinct clades, clearly separating from the reconstructed genomes.

These results are consistent with coverage and BLAST-based analyses, confirming that the detected genomes belong to AdV-12–like and AdV-18–like lineages, respectively.

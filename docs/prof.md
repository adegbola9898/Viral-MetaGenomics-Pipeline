# Progress Update: Genomic Validation and Comparative Analysis of Adenovirus Detections from Animal Metagenomic Samples

## 1. Background

Following the zoonotic oncogenic virus screening, human adenovirus detections emerged as one of the strongest candidate signals requiring read-level validation. The objective of this phase was to determine whether the adenovirus detections represented genuine viral genomic signal, reconstruct viral genomes where possible, and place the recovered sequences within known adenovirus diversity.

This phase was designed to move beyond contig-level detection by using multiple validation layers: raw read mapping, genome coverage profiling, consensus reconstruction, independent de novo assembly, BLAST characterization, phylogenetic analysis, and variant annotation.

## 2. Work Completed

### Sample acquisition

Raw sequencing data were obtained for five adenovirus-positive samples initially selected from the metagenomic screening results.

### Read-level validation

Reference-guided read mapping was performed against an adenovirus reference panel. Two samples showed strong genome-wide adenovirus signal and were prioritized for full downstream validation:

* AIAMA_GOT005_OS_S43 — goat sample, AdV-12-like signal
* AINWZDOG001_S37 — dog sample, AdV-18-like signal

Other samples showed weaker or trace adenovirus signal and were retained as lower-confidence detections.

### Genome reconstruction

Consensus genomes were reconstructed for the two strongest samples using their closest adenovirus references:

* AIAMA_GOT005_OS_S43 relative to Human adenovirus 12 reference X73487.1
* AINWZDOG001_S37 relative to Human adenovirus 18 reference GU191019.1

### Independent de novo assembly validation

MEGAHIT de novo assembly was performed independently from reference-guided mapping. Adenovirus-like contigs were recovered from both validated samples and BLASTed against adenovirus references and study consensus genomes.

### Comparative genomics

BLAST characterization was completed for the reconstructed genomes. Closest matches supported AdV-12-like and AdV-18-like assignments.

### Phylogenetics

Maximum-likelihood phylogenetic analyses were performed using:

* study consensus genomes
* closest GenBank relatives
* African contextual adenovirus sequences
* Nigerian clinical adenovirus sequences
* additional Human mastadenovirus A references
* canine and bovine adenovirus outgroups

### Variant analysis

Variant catalogs were generated for both reconstructed genomes. Coding-region annotation and SNV consequence prediction were performed to identify synonymous and missense variation across adenovirus genes.

## 3. Major Findings

### Finding 1: Recovery of substantial adenovirus genomic sequence

#### Goat sample: AIAMA_GOT005_OS_S43

A near-complete AdV-12-like genome was recovered from the goat sample. Read mapping showed broad genome support, and coverage analysis supported approximately 96.5% genome breadth relative to the AdV-12 reference.

Independent MEGAHIT assembly also recovered multiple AdV-12-like contigs. The largest de novo contig was approximately 9.8 kb and matched the reconstructed AdV-12-like consensus genome at high identity. Additional contigs of approximately 5.5 kb and 4.9 kb also supported the same AdV-12-like signal.

#### Dog sample: AINWZDOG001_S37

A near-complete AdV-18-like genome was recovered from the dog sample. Read mapping and coverage analysis supported approximately 98.06% genome breadth relative to the AdV-18 reference.

Independent de novo assembly recovered multiple AdV-18-like contigs. The largest contig was approximately 11.7 kb and showed very high identity to the reconstructed AdV-18-like consensus genome. Additional contigs of approximately 7.4 kb and 5.4 kb provided further independent support.

Together, these results indicate that the two strongest adenovirus detections are supported by both reference-guided and de novo assembly evidence.

### Finding 2: Phylogenetic placement

The goat-derived genome clustered within the Human mastadenovirus A / AdV-12 lineage.

The dog-derived genome clustered within the Human adenovirus 18 lineage.

Both genomes were distinct from available Nigerian clinical enteric adenovirus sequences, which grouped separately with AdV-40-like viruses. The inclusion of canine and bovine adenoviruses as outgroups supported the placement of the study genomes within human-associated adenovirus diversity rather than non-human mastadenovirus clades.

### Finding 3: African genomic context

The recovered genomes showed relationships to African adenovirus sequences.

The AdV-12-like goat genome grouped near AdV-12-related sequences including an African contextual genome from Kenya.

The AdV-18-like dog genome grouped closely with Tanzanian AdV-18-related genomes.

This places the recovered genomes within broader African adenovirus diversity and provides useful regional context for interpretation.

### Finding 4: Genomic variation

Variant analysis showed that the recovered genomes were not identical to the closest references.

The AdV-12-like goat genome contained:

* 487 total variants
* 474 SNVs
* 13 indels

The AdV-18-like dog genome contained:

* 336 total variants
* 331 SNVs
* 5 indels

Coding-region annotation showed that variants were distributed across multiple adenovirus genes, including:

* hexon
* fiber
* penton
* DNA-binding proteins
* DNA polymerase-related regions
* other structural and replication-associated genes

High-confidence coding SNV analysis showed that synonymous substitutions were more common than missense variants in both genomes, but amino-acid-changing variants were still observed across important structural proteins.

## 4. Interpretation

The analyses confirm that the original adenovirus detections were not isolated contig artifacts. Multiple independent approaches consistently support the presence of adenovirus genomic material closely related to Human adenovirus 12 and Human adenovirus 18.

The strongest evidence comes from the agreement between:

* raw read mapping
* genome-wide coverage profiles
* reference-guided consensus reconstruction
* independent de novo assembly
* BLAST characterization
* maximum-likelihood phylogenetics
* coding variant annotation

At present, these findings support the presence of adenovirus genomic material in animal-associated metagenomic samples. Additional analyses will be required to determine whether this reflects environmental contamination, shared circulation at the human-animal interface, or broader adenovirus ecological dynamics.

The interpretation is therefore deliberately conservative: the current results support genomic detection and reconstruction, but do not yet establish transmission direction, active infection, or epidemiological prevalence.

## 5. Outstanding Questions

### Biological questions

* Are similar AdV-12-like or AdV-18-like lineages circulating in humans or animals in Nigeria?
* Are there published Nigerian human adenovirus genomes related to these lineages?
* What is the epidemiological significance of detecting human-associated adenovirus genomes in animal-associated metagenomic samples?
* Do these detections reflect environmental exposure, sample contamination, human-animal interface circulation, or broader adenovirus ecology?

### Technical questions

* Should the remaining adenovirus-positive samples be fully processed, or should they remain classified as weak/trace detections?
* Can de novo assembly be further improved by host-read depletion or targeted extraction of adenovirus-mapped reads?
* Should additional African adenovirus genomes be added to the phylogenetic context?
* Should genome architecture comparisons be performed between the reconstructed genomes and closest references?
* Should the two consensus genomes be prepared for GenBank submission after final metadata review?

## 6. Current Deliverables

The current analysis has produced:

* validated consensus genomes for two adenovirus-positive samples
* genome-wide coverage profiles
* BLAST characterization tables
* rooted phylogenetic trees
* variant catalogs
* high-confidence coding SNV tables
* SNV consequence plots
* genome-wide variant landscape figures
* de novo assembly validation table
* supplementary manuscript tables
* draft Results, Methods, and Discussion sections

## 7. Next Steps

The immediate next steps are:

1. Finalize manuscript-ready figure legends.
2. Prepare a clean genome metadata table for possible GenBank submission.
3. Review the two consensus FASTA files for naming, completeness, and metadata consistency.
4. Decide whether to submit the two validated genomes to GenBank.
5. Continue interpretation of the weaker adenovirus-positive samples only if needed for the manuscript scope.

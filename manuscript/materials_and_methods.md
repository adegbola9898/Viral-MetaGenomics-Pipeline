# Materials and Methods

## Sample Collection and Sequencing

Metagenomic sequencing datasets were obtained from previously generated animal-derived samples. Raw paired-end FASTQ files were analysed using a custom viral metagenomics workflow developed for adenovirus genome detection, validation, and comparative genomic analysis.

---

## Adenovirus Reference Panel Construction

A reference panel containing representative adenovirus genomes was assembled from GenBank. The panel included Human adenovirus 12 (X73487.1), Human adenovirus 18 (GU191019.1), Human adenovirus 25 (JN226752.1), Human adenovirus 2 (AC_000007.1), and Human adenovirus 41 (MG925783.1).

Reference genomes were downloaded from NCBI and combined into a single FASTA file for initial screening and read-mapping analyses.

---

## Read Mapping and Genome Detection

Sequencing reads were aligned against the adenovirus reference panel using Minimap2.

Mapped reads were processed with SAMtools to generate sorted and indexed BAM files. Mapping statistics were assessed using SAMtools flagstat and idxstats.

Samples showing substantial adenovirus mapping signal were selected for downstream genome reconstruction and validation.

---

## Consensus Genome Reconstruction

For validated samples, reads were remapped against the closest adenovirus reference genome identified during initial screening.

Variant calling was performed using BCFtools, and consensus genomes were generated from compressed VCF files using BCFtools consensus.

The resulting consensus genomes represented the dominant adenovirus sequence present within each sample and were used for comparative genomic and phylogenetic analyses.

---

## Coverage Assessment

Genome coverage profiles were calculated using SAMtools depth.

Coverage breadth and depth statistics were used to evaluate the completeness of recovered genomes. Genome-wide coverage plots were generated in Python using Pandas and Matplotlib.

---

## BLAST Similarity Searches

Consensus genomes were queried against the NCBI nucleotide database using BLASTn.

High-scoring hits were reviewed manually to identify the closest known relatives, determine geographic context, and select additional genomes for phylogenetic analysis.

Representative complete genomes, African contextual sequences, and relevant reference genomes were retained for downstream evolutionary analyses.

---

## Phylogenetic Analysis

A phylogenetic dataset was assembled consisting of:

* Recovered study genomes
* Closest BLAST matches
* Reference adenovirus genomes
* Nigerian clinical adenovirus sequences
* Additional Human mastadenovirus A genomes
* Non-human mastadenovirus outgroups

Sequences were aligned using MAFFT.

Maximum-likelihood phylogenetic inference was performed using IQ-TREE with ultrafast bootstrap support.

Rooting context was provided through inclusion of canine adenovirus type 1, canine adenovirus type 2, and bovine adenovirus 3 genomes.

Phylogenetic trees were visualized in Python using Biopython and Matplotlib.

---

## Variant Identification

Variants were extracted from compressed VCF files using BCFtools query.

Single nucleotide variants (SNVs) and insertion/deletion events (indels) were catalogued relative to the corresponding reference genome.

Genome-wide variant landscape plots were generated to visualize the distribution of variants across each viral genome.

---

## Functional Annotation of Variants

Reference GenBank annotation files corresponding to Human adenovirus 12 (X73487.1) and Human adenovirus 18 (GU191019.1) were downloaded from NCBI.

Custom Python scripts were developed to intersect variant positions with annotated coding sequences (CDS) and determine the affected genes and protein products.

Coding variants were classified as:

* Synonymous
* Missense
* Nonsense
* Stop-loss

Predicted amino acid changes were calculated using reference coding sequences and codon translation.

High-confidence coding variants were subsequently summarized by gene and functional category.

---

## Data Visualization

All downstream analyses and figure generation were performed in Python.

Plots included:

* Genome coverage profiles
* Rooted maximum-likelihood phylogenetic trees
* Variant burden summaries
* SNV consequence distributions
* Genome-wide variant landscape visualizations

Figures were generated using Pandas, Matplotlib, and Biopython.

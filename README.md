# 🧬 One Health Genomic Surveillance of Zoonotic Oncogenic Viruses in Nigeria

## 📌 Overview

This project investigates the presence, validation, and public health relevance of **zoonotic oncogenic viruses** detected in animal-associated metagenomic sequencing data from Nigeria.

Using a structured bioinformatics workflow, we identify viruses with known oncogenic potential, validate their presence at the **read level**, and interpret their significance within a **One Health framework**, focusing on the human–animal interface.

---

## 🎯 Objectives

* Identify **oncogenic viruses** from metagenomic datasets
* Filter for **zoonotic potential** using curated annotations
* Perform **read-level validation** (mapping, coverage analysis)
* Reconstruct and confirm **viral genomes**
* Conduct **phylogenetic analysis** for strain placement
* Analyze **cross-host and geographic patterns**
* Interpret findings in a **Nigeria-specific public health context**

---

## 🧠 Scientific Rationale

Oncogenic viruses contribute significantly to global cancer burden. While many are well-characterized in humans, their **presence and dynamics at the human–animal interface** remain underexplored.

This project addresses key questions:

* Are human-associated oncogenic viruses detectable in animal hosts?
* Do detections represent **true biological signal** or artifacts?
* Are there **structured patterns** across hosts and locations?
* What are the **implications for surveillance and public health in Nigeria**?

---

## 📊 Dataset Summary

* **17,869** viral detection records (contig-level)
* Annotated with **zoonotic status**
* Filtered to:

  * **70** oncogenic candidate viruses
  * **24** zoonotic oncogenic viruses
  * **137** contig-level detections

---

## 🧪 Current Focus: Adenovirus Validation

Initial analysis focuses on **Human adenoviruses** detected in animal samples.

### Key Findings (Preliminary)

| Host | Virus                     | Genome Coverage | Interpretation       |
| ---- | ------------------------- | --------------- | -------------------- |
| Goat | AdV-12 (Mastadenovirus A) | ~96%            | Near-complete genome |
| Dog  | AdV-18 (Mastadenovirus A) | ~98%            | Near-complete genome |

* Mean depth: ~38×
* Mapping rate: ~0.09% (expected for metagenomic viral signal)
* Phylogeny: clustering within **Human mastadenovirus A lineage**

These results support **high-confidence detection of human-like adenoviruses** in animal-associated samples.

---

## 🧬 Analysis Workflow

```text
Metagenomic Detection
        ↓
Oncogenic Filtering
        ↓
Zoonotic Intersection
        ↓
Read-Level Validation (Mapping & Coverage)
        ↓
Genome Reconstruction (Consensus)
        ↓
Phylogenetic Analysis
        ↓
Cross-Sample Pattern Analysis
        ↓
Public Health Interpretation
```

---

## 📁 Repository Structure

```text
├── analysis/           # Stepwise analysis scripts (QC → mapping → phylogeny)
├── results/            # Output tables, figures, intermediate files
├── notebooks/          # Exploratory analyses (Jupyter notebooks)
├── manuscript/         # Living manuscript draft and figures
├── docs/               # Project notes, decisions, and logs
├── data/               # Metadata and data access descriptions (no raw FASTQ)
└── environment/        # Conda environment and dependencies
```

---

## ⚙️ Tools & Methods

* **QC & Preprocessing**: FastQC, fastp
* **Read Mapping**: BWA-MEM / Bowtie2
* **Coverage Analysis**: samtools, bedtools
* **Consensus Generation**: samtools mpileup / bcftools
* **Phylogenetics**: MAFFT, IQ-TREE
* **Statistical Analysis**: Python (pandas, seaborn)

---

## 📦 Data Access

Due to size constraints, raw sequencing data is **not hosted in this repository**.

Data sources include:

* Local storage systems
* Cloud storage (e.g., Google Cloud bucket)

Sample IDs and metadata are available in:

```text
data/metadata/sample_sheet.csv
```

---

## 📈 Project Status

| Module                          | Status                      |
| ------------------------------- | --------------------------- |
| Data curation & filtering       | ✅ Complete                  |
| Adenovirus validation (initial) | ✅ In progress               |
| Identity & phylogeny            | 🚧 Ongoing                  |
| Cross-sample analysis           | ⏳ Pending                   |
| Public health interpretation    | ⏳ Pending                   |
| Manuscript development          | 🚧 Active (living document) |

---

## 🧠 Key Considerations

* Metagenomic viral detections require **careful validation**
* Alternative explanations (e.g., contamination, environmental exposure) are explicitly evaluated
* Interpretations are **cautious and evidence-based**
* Focus is on **exposure and surveillance relevance**, not overclaiming infection

---

## 🚀 Future Work

* Extend validation framework to:

  * Human papillomaviruses (HPV)
  * Merkel cell polyomavirus (MCPyV)
  * Epstein–Barr virus (EBV)
* Perform **comparative cross-virus analysis**
* Strengthen **Nigeria-specific genomic context**
* Finalize **publication-ready manuscript**

---

## 🤝 Acknowledgments

This work is conducted under the supervision of Prof. Anise Happi and collaborators at Redeemer’s University, Institute of Genomics and Global Health.

---

## 📬 Contact

Samuel Adegbola
PhD Research Fellow, Bioinformatics
Redeemer’s University, Nigeria
📧 [adegbola9898@run.edu.ng](mailto:adegbola9898@run.edu.ng)

---

## ⚠️ Disclaimer

This repository contains ongoing research. Results are preliminary and subject to further validation and peer review.

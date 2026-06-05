from Bio import Phylo
import matplotlib.pyplot as plt

treefile = "results/intermediate/phylogeny/adenovirus_outgroup.treefile"
tree = Phylo.read(treefile, "newick")

# Root with non-human mastadenovirus outgroups
outgroup_names = {"AC_000003.1", "AC_000020.1", "NC_001876.1"}

for clade in tree.find_clades():
    if clade.name in outgroup_names:
        tree.root_with_outgroup(clade)
        break

label_map = {
    "AIAMA_GOT005_OS_S43__AdV12_like_consensus": "★ Goat_Nigeria_AdV12-like",
    "AINWZDOG001_S37__AdV18_like_consensus": "★ Dog_Nigeria_AdV18-like",
    "PX485695.1": "PX485695 Tanzania AdV18",
    "PX485696.1": "PX485696 Tanzania AdV18",
    "PQ336882.1": "PQ336882 Kenya AdV12",
    "X73487.1": "X73487 AdV12 ref",
    "NC_001460.1": "NC_001460 AdV-A RefSeq",
    "GU191019.1": "GU191019 AdV18 ref",
    "OR609364.1": "OR609364 AdV18",
    "MG925783.1": "MG925783 AdV41",
    "AC_000003.1": "Outgroup: Canine AdV1",
    "AC_000020.1": "Outgroup: Canine AdV2",
    "NC_001876.1": "Outgroup: Bovine AdV3",
}

def label_func(clade):
    if clade.name is None:
        return None
    if clade.name.startswith("ON1287"):
        return clade.name + " Nigeria AdV40"
    return label_map.get(clade.name, clade.name)

fig = plt.figure(figsize=(18, 14), dpi=300)
ax = fig.add_subplot(1, 1, 1)

Phylo.draw(
    tree,
    label_func=label_func,
    axes=ax,
    do_show=False
)

ax.set_title(
    "Rooted adenovirus phylogeny with Nigerian animal-derived genomes and African context",
    fontsize=14
)

plt.tight_layout()
plt.savefig("results/figures/adenovirus_outgroup_rooted_tree.png", dpi=300, bbox_inches="tight")
plt.savefig("results/figures/adenovirus_outgroup_rooted_tree.pdf", bbox_inches="tight")

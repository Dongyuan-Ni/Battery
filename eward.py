from pymatgen.core import Structure, Lattice, Element
from pymatgen.transformations.standard_transformations import OrderDisorderedStructureTransformation
from pymatgen.analysis.structure_matcher import StructureMatcher
from pymatgen.io.vasp.inputs import Poscar
import os

def GS(
        file,           # Carbon POSCAR file (without Na ion)
        sites,          # Adsorption sites
        n,              # Na ion concentration
        c,              # Average charge transfer to the carbon system
        N_structures,   # Number of structures generated for each concentration
        Structure_name,
        Ranked_list     # Length of OrderDisorderedStructureTransformation's list
):

######################CORE CODE#######################
    struct = Structure.from_file(file)
    for i in range(len(struct)):
        struct[i] = {"C"+str(c)+"-": 1}

    for site in sites:
        struct.append({"Na+":n}, site)

    trans = OrderDisorderedStructureTransformation()
    ss = trans.apply_transformation(struct, return_ranked_list=Ranked_list)
    # matcher = StructureMatcher(stol=0.01)
    matcher = StructureMatcher(stol=0.1)
    groups = matcher.group_structures([d["structure"] for d in ss])
######################CORE CODE#######################

    print("Lens of all sym-no-equi types: {}".format(len(groups)))

######################EWALD ENERGY####################
    groups_list_idx = []
    energy_list_idx = [0]
    energy_list = []
    for i in range(len(groups)):
        groups_list_idx.append(len(groups[i]))
    for i in range(len(groups_list_idx)-1):
        energy_list_idx.append(sum(groups_list_idx[:i+1]))
    for i in energy_list_idx:
        energy_list.append(ss[i]['energy_above_minimum'])
######################EWALD ENERGY####################


#################DUMP STRUCTURE#######################
    os.mkdir(Structure_name+"-"+str(n))
    for idx, d in enumerate(groups):
        if idx == N_structures:
            break
        Poscar(d[0]).write_file(filename=Structure_name+"-"+str(n)+"/"+str(energy_list[idx])+".vasp")
#################DUMP STRUCTURE#######################

def main():

################INPUT#################################
    file = 'Empty.vasp'
    s = Structure.from_file('Full.vasp')
    sites = s.frac_coords[:18]
    # n = [0.167]                                 # Na ion concentration
    # n = [0.333]
    # n = [0.500]
    # n = [0.667]
    n = [0.833]
    NC = 80                                     # Number of carbon atoms in the structure
    N_structures = 100                       # Number of structures generated for each concentration
    Structure_name = "c"
    Ranked_list = 100                        # Length of OrderDisorderedStructureTransformation's list
################INPUT#################################

    c = [n_i * len(sites) / NC for n_i in n]
    for k in range(len(n)):
        print("Concentration: {}".format(n[k]))
        GS(file, sites, n[k], c[k], N_structures, Structure_name, Ranked_list)

if __name__ == '__main__':
    main()

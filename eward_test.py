from pymatgen.core import Structure, Lattice, Element
# struct = Structure.from_file('Empty.vasp')
struct = Structure.from_file('Full.vasp')
print(struct)
# c = 0.005
# N_B = 36
# for i in range(N_B):
#     struct[i] = {"B"+str(c)+"-": 1}
# for i in range(N_B, len(struct)):
#     struct[i] = {"P"+str(c)+"-": 1}
# print(struct)

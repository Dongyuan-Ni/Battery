import numpy as np
from itertools import *



adp0 = -1685.14871165
adp1 = -1696.56788306
adp2 = -1706.42117556
adp3 = -1716.10917578
adp4 = -1724.42025857
adp5 = -1733.06031583
adp6 = -1738.68863201

# adp0 = -1685.15
# adp1 = -1696.57
# adp2 = -1706.42
# adp3 = -1716.11
# adp4 = -1724.42
# adp5 = -1733.06
# adp6 = -1738.69

# Na Concentration
x1 = 0
x2 = 5

#################
na = -2.90 / 2
out0 = -(adp1 - adp0 - (x2 - x1) * na) / (x2 - x1)
out1 = -(adp2 - adp1 - (x2 - x1) * na) / (x2 - x1)
out2 = -(adp3 - adp2 - (x2 - x1) * na) / (x2 - x1)
out3 = -(adp4 - adp3 - (x2 - x1) * na) / (x2 - x1)
out4 = -(adp5 - adp4 - (x2 - x1) * na) / (x2 - x1)
out5 = -(adp6 - adp5 - (x2 - x1) * na) / (x2 - x1)

#################
print(out0)
print(out1)
print(out2)
print(out3)
print(out4)
print(out5)
print((out0 + out1 + out2 + out3 + out4 + out5) / 6)
print((out0 + out1 + out2 + out3 + out4) / 5)

# e1 = (adp1 - adp0 - 3 * na)/3
# e2 = (adp2 - adp0 - 6 * na)/6
# e3 = (adp3 - adp0 - 9 * na)/9
# e4 = (adp4 - adp0 - 12 * na)/12
# e5 = (adp5 - adp0 - 15 * na)/15
# print(e1)
# print(e2)
# print(e3)
# print(e4)
# print(e5)

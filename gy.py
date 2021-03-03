import numpy as np
import pprint
np.set_printoptions(precision=3)
pp = pprint.PrettyPrinter(indent=4)

#непрерывная цепь
#pi = (1, 0, 0, 0)
L = np.array([[-4-7, 4, 7, 0],
             [6, -6-1-2, 1, 2],
             [8, 9, -8-9-4, 4],
             [0, 1, 3, -3-1]])

for i in range(21):
    pp.pprint(np.linalg.matrix_power(P, i))
    print("."*50)


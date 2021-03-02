import numpy as np
import pprint
np.set_printoptions(precision=5)
pp = pprint.PrettyPrinter(indent=4)
P = np.array([[0.1, 0.7, 0.1, 0.1],
             [0, 0, 1, 0],
             [0, 0.8, 0, 0.2],
             [0.1, 0.1, 0.7, 0.1]])
for i in range(501):
    pp.pprint(np.linalg.matrix_power(P, i))
    print("."*50)
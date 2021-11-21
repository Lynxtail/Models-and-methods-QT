import numpy as np

lmbd = 3
mu_1 = 1
mu_2 = 2
N = 2

states = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)]
print(f'Пространство состояний:\n{states}')

coef = np.zeros((10,10))

coef[0][0] = -lmbd
coef[0][2], coef[1][3], coef[4][6], coef[7][9] = [mu_1]*4
coef[0][1], coef[2][3], coef[5][6], coef[8][9] = [mu_2]*4
coef[1][1] = -(lmbd + mu_2)
coef[2][2] = -(lmbd + mu_1)
coef[2][0], coef[3][2], coef[3][1], coef[5][3],\
coef[6][5], coef[6][4], coef[8][6], coef[9][8],\
coef[9][7] = [lmbd]*9
coef[3][3], coef[4][4], coef[5][5], coef[6][6],\
coef[7][7], coef[8][8] = [-(lmbd + mu_1 + mu_2)]*6
coef[3][4], coef[3][5], coef[6][7], coef[6][8] = [mu_1 + mu_2]*4
coef[9][9] = -(mu_1 + mu_2)

print(f'Матрица коэффициентов СЛАУ:\n{coef}')

E = np.eye(10)
A = coef.T - E
A[9, :] = np.ones(10)
# A = np.vstack((A, np.ones(10)))

B = [[0]]*9
B.append([1])

p = np.linalg.solve(A, B)
print(f'Вектор стационарных вероятностей:\n{p}')
print(f'Сумма компонент вектора p = {np.sum(p)}')

p_refuse = p[-1]
print(f'А) Вероятность отказа: {p_refuse}')

count = float((1 - p[-1]) * 100)
print(f'Б) Доля выполненых заказов: {count:.3f}%')

p_over_1 = 1 - p[0] - p[1]
p_over_2 = 1 - p[0] - p[2]
print(f'В) Вероятность загруженности первого потока: {p_over_1}\n\
Вероятность загруженности второго потока: {p_over_2}')

n_1 = (p[2] + p[3] + p[4]) + 2*(p[5] + p[6] + p[7]) + 3*(p[8] + p[9])
n_2 = (p[1] + p[3] + p[5]) + 2*(p[4] + p[6] + p[8]) + 3*(p[7] + p[9])
n_ = 2*p[3] + 2*2*p[6] + 2*3*p[9] + (p[1] + p[2]) + 3*(p[4] + p[5]) + 5*(p[7] + p[8])
print(f'Г) Среднее число машин, находящихся в первом потоке: {n_1}\n\
Среднее число машин в мастерской: {n_}')

# p_tmp = []
# i = 0
# while i < 10:
#     if i % 3 == 0:
#         p_tmp.append(p[i])
#         i += 1
#     else:
#         p_tmp.append(p[i]+p[i+1])
#         i += 2
# p_tmp = np.array(p_tmp)

# h = sum([s*p_tmp[s] for s in range(3)]) + 2 * sum([p_tmp[s] for s in range(3, 7)])
# print(h)

h = 0 * p[0] + 1 * (p[1] + p[2]) + 2 * (p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9])
# print(h)
b = n_ - h
print(f'Д) Среднее число машин, ожидающих обслуживания, в первом и во втором потоках: {b}')

t_free = float(p[0]*100)
print(f'Е) Доля времени простоя: {t_free:.3f}%')


import numpy as np

lmbd = 4
mu_1 = 1
mu_2 = 2
kappa = 3
b = 1
N = 2

states = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 3), (1, 2), (2, 1)]
print(f'Пространство состояний:\n{states}')

def a_f(n, m):
    res = 1
    for i in range(m):
        res *= n + i
    return res

def Q(k):
    return a_f(k, 1) \
        + a_f(k - 1, 2) * a_f(lmbd + 1/b + 1, 1) * b/lmbd \
            + a_f(k - 2, 3) * a_f(lmbd + 1/b + 1, 2) * (b/lmbd)**2 

def p_all(k):
    return lmbd / (lmbd + (1 + b*lmbd) * Q(k))

def p_ref(k):
    return (lmbd * (1 + b * Q(k)) / (lmbd + (1 + b * lmbd) * Q(k)))


coef = np.zeros((7,7))

coef[0][0] = -lmbd
coef[0][1], coef[1][2], coef[2][3], coef[3][3], \
coef[4][5], coef[5][6] = 1., 2., 3., -3., 1., 2.
coef[1][1], coef[2][2] = (-lmbd - 1.), (-lmbd - 2.)
coef[1][4], coef[2][5], coef[3][6] = [1/b]*3
coef[4][4], coef[5][5], coef[6][6] = -1/b, (-1/b - 1), (-1/b - 2)
coef[4][0], coef[5][1], coef[6][2] = [lmbd]*3
print(f'Матрица коэффициентов СЛАУ:\n{coef}')

E = np.ones((7, 7))
A = coef - E

B = [[-1]]*7
# B.append([1])

ans = np.linalg.solve(A, B)
p = ans[:4]
q = ans[4:]
print(f'Вектор стационарных вероятностей пребывания системы в состоянии (i, 0):\n{p}')
print(f'Сумма компонент вектора p = {np.sum(p)}')
print(f'Вектор стационарных вероятностей пребывания системы в состоянии (j - 1, {kappa} - j + 1):\n{q}')
print(f'Сумма компонент вектора q = {np.sum(q)}')
print(f'Сумма компонент векторов p и q = {np.sum(p) + np.sum(q)}')

count1 = float((1 - p_ref(kappa)) * 100)
print(f'А) Доля проверенных во втором этапе изделий: {count1:.3f}%')

n = 1 * p[1] + 2 * p[2] + 3 * (p[3] + np.sum(q))
print(f'Б) М. о. количества изделий, которые находятся на первом и на втором этапах контроля качества продукции: {n}')

print(f'В) Вероятность отказа в проверке изделия: {p_ref(kappa)}')
count2 = float(((3 - 1 + 1) * q[0] + (3 - 2 + 1) * q[1] + (3 - 3 + 1) * q[2]) * 100 / 3)
print(f'Г) Доля приборов, занятых на первом этапе контроля качества продукции: {count2:.3f}%')
print(f'Доля приборов, занятых на втором этапе контроля качества продукции: {100 - count2:.3f}%')

print(f'Д) Вероятность того, что все контрольно-проверочные комплексы заняты проверкой изделий на втором этапе: {p_all(kappa)}')

print(f'Е) Вероятность того, что 0, 1, 2 или все приборы заняты выполнением первого этапа проверки изделия:')
print(f'Вероятность, что 0 приборов заняты выполнением первого этапа проверки: {1 - np.sum(q)}')
[print(f'Вероятность, что {kappa - i} приборов заняты выполнением первого этапа проверки: {q[i]}') for i in range(kappa)]

# print(p_all(kappa))
# print(Q(kappa))
# print(f'{a_f(kappa, 1)} + {a_f(kappa - 1, 2)} \
# * {a_f(lmbd + 1/b + 1, 1)} \
# * {b/lmbd} + {a_f(kappa - 2, 3)} \
# * {a_f(lmbd + 1/b + 1, 2)} * {(b/lmbd)**2}')
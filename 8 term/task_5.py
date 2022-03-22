import numpy as np
from pprint import pprint


def get_p(M, v):
    return np.linalg.solve(M, v)

def get_matrix(k):
    M = np.zeros((k + 1, k + 1))
    M[0] = np.ones(k + 1)
    for i in range(1, k + 1):
        M[i][i - 1] = i
        M[i][i] = -i
        if i >= 4:
            M[i][i - 4] = -1
    print()
    pprint(M)
    return M

k = 5
m = 3
lambda_ = 5
mu = 5 
alpha = lambda_ / mu
M = get_matrix(k)
v = [1] + [0] * k

p = get_p(M, v)
print(f'Стационарные вероятности состояний системы: {p}')

# а) вероятность потери информации
h = sum([n * p[n] for n in range(k + 1)])
p_ref = 1 - h / (alpha * m)
print(f'А) Вероятность потери информации: {p_ref}')

# б) математическое ожидание числа каналов, занятых обработкой информации 
print(f'Б) М.о. числа каналов, занятых обслуживанеим: {h}')

# в) коэффициент загрузки вычислительной машины 
print(f'В) Коэффициент загрузки вычислительной машины: {h / k}')

# г) коэффициент простоя каналов обработки информации
print(f'Г) Коэффициент простоя каналов обработки информации: {1 - h / k}')

# Определить, сколько каналов обработки информации должна иметь вычислительная машина,
# чтобы вероятность потери информации была не более 5%
while p_ref >= 0.05:
    k += 1
    M = get_matrix(k)
    v = [1] + [0] * k
    p = get_p(M, v)
    h = sum([n * p[n] for n in range(k + 1)])
    p_ref = 1 - h / (alpha * m)
    print(f'\nВероятность потери информации при {k} каналов равна {p_ref}')
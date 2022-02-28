# M/M/k с групповым обслуживанием
# k = 4 самосвала по 2 м3
# замес 10 м3 в 2 часа
# t_wait = 2 часа

# lambda = 10/2 м3 в час 
# mu = 2/10 м3 в час

from math import factorial, exp
import numpy as np
import matplotlib.pyplot as plt

def get_r(alpha, beta):
    eps = .00000001
    r = 1
    while ((alpha / beta)**r / factorial(r-1)) * exp(alpha / beta) > eps:
        r += 1
    return r

def prod(k, s, beta):
    prod = 1
    for m in range(1, s + 1):
        prod *= (k + m * beta)
    return prod


def get_p_0(k, alpha, beta):
    res_1 = sum([(alpha ** n / factorial(n)) for n in range(0, k + 1)])
    res_2 = alpha ** k / factorial(k)
    res_3 = sum([alpha ** s / prod(k, s, beta) for s in range(1, r + 1)])
    res = 1 / (res_1 + res_2 * res_3)
    return res


def get_p_n(n, alpha, p_0):
    return (alpha**n / factorial(n)) * p_0


def get_p_ks(k, s, alpha, beta, p_0):
    res = ((alpha**(k + s)) / (factorial(k) * prod(k, s, beta))) * p_0
    return res


lambda_ = 5
mu = 0.2
k = 4
nu = 1 / (k * mu)
t_wait = 2

alpha = lambda_ / mu
beta = nu / mu

r = get_r(alpha, beta)
print(f'r = {r}')

# а) вероятность того, что 1, 2 или все самосвалы возьмут бетон из замеса (т. е. эти самосвалы не находятся в рейсе); 
print('A) Вероятность того, что 1, 2 или все самосвалы возьмут бетон из замеса (т. е. эти самосвалы не находятся в рейсе):')
p_0 = get_p_0(k, alpha, beta)
[print(f'\t{k - n - 1} самосвалы: {get_p_n(n, alpha, p_0)}') for n in [2, 1]] 
print(f'\tВсе самосвалы: {p_0}')

# б) среднее число самосвалов, которые возьмут бетон из замеса; 
h = sum([n * get_p_n(n, alpha, p_0) for n in range(1, k + 1)]) + \
    k * sum([get_p_ks(k, s, alpha, beta, p_0) for s in range(1, r + 1)])
print(f'Б) Среднее число самосвалов, которые возьмут бетон из замеса: {h}')

# в) количество бетона, которое будет израсходовано на свою стройку, и количество бетона, отданного другим организациям; 
b = sum([s * get_p_ks(k, s, alpha, beta, p_0) for s in range(1, r + 1)])
p_ref = 1 - h / alpha
mean_count_finished = lambda_ * (1 - p_ref)
mean_count_refuse = lambda_ * p_ref
print(f'В) Количество бетона, которое будет израсходовано на свою стройку: {mean_count_finished}')
print(f'   Количество бетона, отданного другим организациям: {mean_count_refuse}')

# г) вероятность того, что весь бетон будет отдан другим строительным организациям; 
print(f'Г) Вероятность того, что весь бетон будет отдан другим строительным организациям: {p_ref}')

# д) долю машин стройки, используемых для перевозки бетона, и долю машин, простаивающих в ожидании загрузки бетона; 
print(f'Д) Доля машин стройки, используемых для перевозки бетона: {(1 - p_0) * 100}%')
print(f'   Доля машин, простаивающих в ожидании загрузки бетона: {p_0 * 100}%')

# е) вероятность простоя самосвалов.
print(f'Е) Вероятность простоя самосвалов: {p_0}')

# Определить долю машин стройки, используемых для перевозки бетона, в зависимости от 
print()
# а) объема одного замеса бетона, который меняется – увеличивается на 10, 20, …, 100 процентов (построить график зависимости);
lambdas = np.arange(0.1, 1.1, 0.1) * lambda_ + lambda_
print(f'А) Увеличение объёма одного замеса бетона: {lambdas}')
p_s = []
for lambda_tmp in lambdas:
    alpha = lambda_tmp / mu
    p_s.append(1 - get_p_0(k, alpha, beta))
print(f'   Доля машин стройки, используемых для перевозки бетона: {p_s}')
plt.plot(lambdas, p_s)
plt.title('Доля машин на стройке, используемых для перевозки бетона,\nв зависимости от объёма одного замеса бетона')
plt.xlabel('Объём, м^3')
plt.ylabel('Машины, %')
plt.show()

# б) изменения количества единиц занятых на перевозке бетона самосвалов – увеличения, но не более, чем в 2 раза (построить график зависимости)
kappas = np.arange(5, k*2+1)
print(f'Б) Увеличение числа занятых на перевозке самосвалов: {kappas}')
p_s = []
alpha = lambda_ / mu
for kappa_tmp in kappas:
    nu = 1 / (kappa_tmp * mu)
    beta = nu / mu
    p_s.append(1 - get_p_0(kappa_tmp, alpha, beta))
print(f'   Доля машин стройки, используемых для перевозки бетона: {p_s}')
plt.autoscale(tight=True)
plt.plot(kappas, p_s)
plt.title('Доля машин на стройке, используемых для перевозки бетона,\nв зависимости от числа выделенных на перевозку самосвалов')
plt.xlabel('Число выделенных машин')
plt.ylabel('Доля используемых машин, %')
plt.show()

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

def prod_alpha_1(alpha, l):
    prod = 1
    for m in range(0, l):
        prod *= (alpha + m)
    return prod

def prod_alpha_2(alpha, l):
    prod = 1
    for m in range(1, l+1):
        prod *= (alpha + m)
    return prod


def prod_beta(k, s, beta):
    prod = 1
    for r in range(1, s + 1):
        prod *= (k + r * beta)
    return prod


def get_p_0(k, alpha, beta):
    res_1 = prod_alpha_2(alpha, k) / factorial(k)
    res_2 = prod_alpha_1(alpha, k) / factorial(k)
    res_3 = sum([alpha ** s / prod_beta(k, s, beta) for s in range(1, r + 1)])
    res = 1 / (res_1 + res_2 * res_3)
    return res


def get_p_n(n, alpha, p_0):
    return (prod_alpha_1(alpha, n) / factorial(n)) * p_0


def get_p_ks(k, s, alpha, beta, p_0):
    res = ((alpha**s * prod_alpha_1(alpha, k)) / (factorial(k) * prod_beta(k, s, beta))) * p_0
    return res


k = 4
lambda_ = 1 / 2
mu = 1 / 5
nu = 1 / 2

alpha = lambda_ / mu
beta = nu / mu

r = get_r(alpha, beta)
print(f'r = {r}')

# а) вероятность того, что 1, 2 или все самосвалы возьмут бетон из замеса (т. е. эти самосвалы не находятся в рейсе); 
print('A) Вероятность того, что 1, 2 или все самосвалы возьмут бетон из замеса (т. е. эти самосвалы не находятся в рейсе):')
p_0 = get_p_0(k, alpha, beta)
for n in [1, 2]:
    # tmp = p_0
    # tmp += sum([get_p_n(l, alpha, p_0) for l in range(k - n + 1)])
    tmp = get_p_n(k - n, alpha, p_0)
    print(f'\t{n} самосвал(-а): {tmp}') 
print(f'\tВсе самосвалы: {p_0}')
# вер-ть, что 1 самосвал свободен -- p0 + p1 + p2 + p3
# вер-ть, что 2 самосвала свободны -- p0 + p1 + p2
# вер-ть, что 4 самосвала свободны -- p0

# б) среднее число самосвалов, которые возьмут бетон из замеса; 
def get_h(alpha, p_0, k):
    h = sum([n * get_p_n(n, alpha, p_0) for n in range(k + 1)]) + \
        k * (1 - sum([get_p_n(n, alpha, p_0) for n in range(k + 1)]))
    return h

# м.о. занятых приборов?
h = get_h(alpha, p_0, k)
print(f'Б) Среднее число самосвалов, которые возьмут бетон из замеса: {k - h}')

# в) количество бетона, которое будет израсходовано на свою стройку, и количество бетона, отданного другим организациям; 
b = sum([s * get_p_ks(k, s, alpha, beta, p_0) for s in range(1, r + 1)])
p_ref = beta / alpha * b
mean_count_finished = lambda_ * (1 - p_ref)
mean_count_refuse = lambda_ * p_ref
print(f'В) Количество бетона, которое будет израсходовано на свою стройку: {mean_count_finished}')
print(f'   Количество бетона, отданного другим организациям: {mean_count_refuse}')

# г) вероятность того, что весь бетон будет отдан другим строительным организациям; 
# вероятность отказа?
# p_k
ans = get_p_n(k, alpha, p_0) + sum([get_p_ks(k, s, alpha, beta, p_0) for s in range(1, r + 1)])
print(f'Г) Вероятность того, что весь бетон будет отдан другим строительным организациям: {ans}')

# д) долю машин стройки, используемых для перевозки бетона, и долю машин, простаивающих в ожидании загрузки бетона; 
def k_h(h, k):
    return h / k

def k_g(k, h):
    return (k - h) / k

print(f'Д) Доля машин стройки, используемых для перевозки бетона: {k_h(h, k) * 100}%')
print(f'   Доля машин, простаивающих в ожидании загрузки бетона: {k_g(k, h) * 100}%')

# е) вероятность простоя самосвалов.
print(f'Е) Вероятность простоя самосвалов: {p_0}')

# Определить долю машин стройки, используемых для перевозки бетона, в зависимости от 
print()
# а) объема одного замеса бетона, который меняется – увеличивается на 10, 20, …, 100 процентов (построить график зависимости);
# V = 10 м^3
V = np.arange(0.1, 1.1, 0.1) * 10 + 10
mus = 2 / V
print(f'А) Увеличение объёма одного замеса бетона: {V}')
p_s = []
for mu_tmp in mus:
    alpha = lambda_ / mu_tmp
    beta = nu / mu_tmp
    p_s.append(k_h(get_h(alpha, get_p_0(k, alpha, beta), k), k) * 100)
print(f'   Доля машин стройки, используемых для перевозки бетона: {p_s}')
plt.autoscale(tight=True)
plt.plot(V, p_s)
plt.title('Доля машин на стройке, используемых для перевозки бетона,\nв зависимости от объёма одного замеса бетона')
plt.xlabel('Объём, м^3')
plt.ylabel('Машины, %')
plt.show()

# б) изменения количества единиц занятых на перевозке бетона самосвалов – увеличения, но не более, чем в 2 раза (построить график зависимости)
kappas = np.arange(5, k*2+1)
print(f'Б) Увеличение числа занятых на перевозке самосвалов: {kappas}')
p_s = []
alpha = lambda_ / mu
beta = nu / mu
for kappa_tmp in kappas:
    p_s.append(k_h(get_h(alpha, get_p_0(kappa_tmp, alpha, beta), kappa_tmp), kappa_tmp) * 100)
print(f'   Доля машин стройки, используемых для перевозки бетона: {p_s}')
plt.autoscale(tight=True)
plt.plot(kappas, p_s)
plt.title('Доля машин на стройке, используемых для перевозки бетона,\nв зависимости от числа выделенных на перевозку самосвалов')
plt.xlabel('Число выделенных машин')
plt.ylabel('Доля используемых машин, %')
plt.show()

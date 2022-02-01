# M/M/k/B
# t_wait = 10
# lambda = 2
# mu = 0.2
# k = 2

from math import factorial, exp


def get_r(alpha, beta):
    eps = .00000001
    r = 1
    while ((alpha / beta)**r / factorial(r-1)) * exp(alpha / beta) > eps:
        r += 1
    return r


def prod(k, s, beta):
    prod = 1
    for m in range(1, s + 1):
        prod *= (k + (k + m) * beta)
    return prod


def get_p_0(k, alpha, beta, r):
    res_1 = sum([alpha ** n / (factorial(n) * (1 + beta)**k) for n in range(0, k + 1)])
    res_2 = alpha ** k / (factorial(k) * (1 + beta)**k)
    res_3 = sum([alpha ** s / prod(k, s, beta) for s in range(1, r + 1)])
    res = 1 / (res_1 + res_2 * res_3)
    return res


def get_p_n(n, alpha, p_0):
    return (alpha**n / factorial(n) * (1 + beta)**n) * p_0


def get_p_ks(k, s, alpha, beta, p_0):
    res = ((alpha**(k + s)) / (factorial(k) * (1 + beta)**k * prod(k, s, beta))) * p_0
    return res


lambda_ = 2.
mu = .2
nu = .1
k = 2

alpha = lambda_ / mu
beta = nu / mu

r = get_r(alpha, beta)
print(f'r = {r}')

# а) долю времени, когда все ЭВМ свободны от проведения расчетов
p_0 = get_p_0(k, alpha, beta, r)
print(f"А) Доля времени, когда все ЭВМ свободны от проведения расчетов: {p_0}")

# б) долю времени, когда одна из ЭВМ будет занята расчетом, а другие свободны
p_1 = get_p_n(1, alpha, p_0)
print(f"Б) Доля времени, когда одна из ЭВМ будет занята расчетом, а другие свободны: {p_1}")

# в) вероятность того, что все ЭВМ будут работать одновременно, и не поступило новых данных для проведения расчетов
p_k = get_p_n(k, alpha, p_0)
print(f"В) Вероятность того, что все ЭВМ будут работать одновременно, и не поступило новых данных для проведения расчетов: {p_k}")

# г) вероятность отказа поступившим заказам на проведение метеорологических расчетов
h = sum([n * get_p_n(n, alpha, p_0) for n in range(1, k + 1)]) + \
    k * sum([get_p_ks(k, s, alpha, beta, p_0) for s in range(1, r + 1)])
b = sum([s * get_p_ks(k, s, alpha, beta, p_0) for s in range(1, r + 1)])
p_ref = 1 - h / alpha
print(f"Г) Вероятность отказа поступившим заказам на проведение метеорологических расчетов: {p_ref}")

# д) среднее число заказов, находящихся в вычислительном центре и ожидающих проведения метеорологических расчетов
print(f"Д) Среднее число заказов, ожидающих проведения метеорологических расчетов: {b}")
print(f"   Среднее число заказов, находящихся в вычислительном центре: {(b + h)}")

# е) долю ЭВМ, простаивающих в вычислительном центре
g = k - h
k_g = g / k
print(f"E) Доля ЭВМ, простаивающих в вычислительном центре: {k_g}")

# Определить число ЭВМ, необходимое,
# чтобы вероятность отказа поступившим заказам на проведение метеорологических расчетов не превышала 0,1
print('Определение числа ЭВМ для желаемого значения вероятности отказа требованию')
p_ref_max = .1
print('\tвероятность отказа\tколичество ЭВМ')
while p_ref >= p_ref_max:
    k += 1
    p_0 = get_p_0(k, alpha, beta, r)
    b = sum([s * get_p_ks(k, s, alpha, beta, p_0) for s in range(1, r + 1)])
    p_ref = b * (beta / alpha)
    print(f"\t{p_ref:.3f}\t\t\t{k}")

print(f"При {k} ЭВМ вероятность отказа будет не превышать заданное значение ({p_ref_max})")

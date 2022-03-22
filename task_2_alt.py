# M/M/k/B
# t_wait = 1
# lambda = 2.5*2
# mu = 4
# k = 2
# B = 5


from math import factorial


def prod(k, s, beta):
    prod = 1
    for m in range(1, s + 1):
        prod *= (k + m * beta)
    return prod


def get_p_0(k, alpha, beta, B):
    res_1 = sum([(alpha ** n / factorial(n)) for n in range(0, k + 1)])
    res_2 = alpha ** k / factorial(k)
    res_3 = sum([alpha ** s / prod(k, s, beta) for s in range(1, B + 1)])
    res = 1 / (res_1 + res_2 * res_3)
    return res


def get_p_n(n, alpha, p_0):
    return (alpha**n / factorial(n)) * p_0


def get_p_ks(k, s, alpha, beta, p_0):
    res = ((alpha**(k + s)) / (factorial(k) * prod(k, s, beta))) * p_0
    return res

# интенсивность входящего потока
lambda_ = 3.8
# интенсивность обслуживания
mu = 3
# интенсивность ухода требований
nu = 1 / 2
k = 2
# вместимость очереди
B = 5

alpha = lambda_ / mu
beta = nu / mu

# а) вероятность того, что все бригады будут сидеть без дела из-за отсутствия овощей; 
p_0 = get_p_0(k, alpha, beta, B)
print(f'А) Вероятность того, что все бригады будут сидеть без дела: {p_0}')

# б) вероятность того, что привезенные овощи не будут своевременно обработаны; 
p_ref = (alpha - k + sum([(k - n) * get_p_n(n, alpha, p_0) for n in range(k+1)])) / alpha
print(f'Б) Вероятность того, что привезенные овощи не будут своевременно обработаны: {p_ref}')

# в) среднее число бригад, занятых обработкой овощей; 
h = sum([n * get_p_n(n, alpha, p_0) for n in range(1, k + 1)]) + \
    k * sum([get_p_ks(k, s, alpha, beta, p_0) for s in range(1, B + 1)])
print(f'в) Среднее число бригад, занятых обработкой овощей: {h}')

# г) долю бригад, простаивающих или занятых обработкой овощей;
g = k - h
print(f'г) Доля простаивающих бригад: {g/k * 100 :.3f}%')
print(f'   Доля занятых обработкой овощей бригад: {h/k * 100 :.3f}%')

# д) среднее число тонн овощей, обработанных за сутки, и среднее число тонн овощей, потерянных за сутки из-за их несвоевременной обработки;
mean_count_finished = lambda_ * (1 - p_ref)
mean_count_refuse = lambda_ * p_ref
print(f'Д) Среднее число тонн овощей, обработанных за сутки: {mean_count_finished}')
print(f'   Среднее число тонн овощей, потерянных за сутки из-за их несвоевременной обработки: {mean_count_refuse}')

# е) среднее число тонн овощей, ожидающих обработки
b = sum([s * get_p_ks(k, s, alpha, beta, p_0) for s in range(1, B + 1)])
print(f'Е) Среднее число тонн овощей, ожидающих обработки: {b}')

# Определить необходимое количество бригад, 
# чтобы потери привезенных овощей из-за 
# несвоевременной их обработки составляли не более 10 %

print('Определение числа бригад для желаемого значения потерь овощей')
p_ref_max = .1
print('\tвероятность отказа\tколичество бригад')
while p_ref >= p_ref_max:
    k += 1
    p_0 = get_p_0(k, alpha, beta, B)
    p_ref = (alpha - k + sum([(k - n) * get_p_n(n, alpha, p_0) for n in range(k+1)])) / alpha
    print(f"\t{p_ref:.3f}\t\t\t{k}")

print(f"При {k} бригадах доля потерянных овощей составляет {p_ref}")

n = 5
lmbd = [1, 2, .5, 1.1, 3]
v = [.2, .1, .1, .15, .01]
c = [5, 4, 3, 2, 1]
d = [2/v[i]**2 for i in range(n)]
mu = [1 / v[i] for i in range(n)]
v_2 = [d[i] + v[i] ** 2 for i in range(n)]
psi = [lmbd[i] / mu[i] for i in range(n)]
s = 0
R_N = []
for i in range(n):
    s += psi[i]
    R_N.append(s)
[print(f'Коэффициент использования прибора (класс {i+1}): {R_N[i]:.1f}') for i in range(n)]

delta = [v_2[i] / (2 * v[i]) for i in range(n)]
sigma = []
s = 0
for i in range(n):
    s += psi[i] * delta[i]
    sigma.append(s)

w = [sigma[0] / (1 - R_N[0])]
for i in range(1, n):
    w.append(sigma[i] / ((1 - R_N[i - 1]) * (1 - R_N[i])))
[print(f'Средняя продолжительность ожидания обработки требований {i+1} класса: {w[i]:.1f}') for i in range(n)]

w_rand = sum([w[i] * lmbd[i] / sum(lmbd) for i in range(n)])
print(f'Средняя продолжительность ожидания обработки требований из общего потока:\n{w_rand:.1f}')

F = sum([c[i] * lmbd[i] * w[i] for i in range(n)])
print(f'F: {F:.1f}')

# условия оптимизации абсолютных приоритетов
cond1 = [c[i] / v[i] for i in range(n)]

cond2 = [2 * v[i] * c[i] / v_2[i] for i in range(n)]

print('\tВторое условие\tПервое условие')
for i in range(n):
    print(f'i = {i+1}:\t{round(cond2[i], 3)}\t\t{round(cond1[i], 3)}')
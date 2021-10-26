
n = 3
lmbd = [.2, .3, .1]
v = [2., 1., 2.]
d = .5

mu = [1 / v[i] for i in range(n)]
v_2 = [d + v[i] ** 2 for i in range(n)]
psy = [lmbd[i] / mu[i] for i in range(n)]
R_N = sum(psy)
print(f'Коэффициент использования прибора (вне зависимости от класса требования): {R_N:.1f}')

w = 0.5 * sum([v_2[i] * lmbd[i] for i in range(n)]) / (1 - R_N)
print(f'Средняя продолжительность ожидания в каждой очереди: {w:.1f}')
print(f'Среднее время ожидания произвольного заказа на обслуживание: {w:.1f}')

b = [lmbd[i] * w for i in range(len(lmbd))]
[print(f'Среднее число заказов в {i + 1} очереди: {b[i]:.1f}') for i in range(len(b))]
print(f'Средняя длина очереди: {sum(b):.1f}')
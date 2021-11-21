mu_1 = 9
mu_2 = 6
lmbd = 12
phi = 0.5

alpha = lmbd / (mu_1 + mu_2)
print(f'alpha = {alpha}')
beta = mu_2 / mu_1
print(f'beta = {beta}')

t_1 = alpha / (1 + 2 * alpha)
t_2 = 1 / beta
t_3 = 1 + (1 + beta ** 2) * alpha - (1 - beta ** 2) * phi

T = 10000
p_00 = (1 - alpha) / (1 + t_1 * t_2 * t_3)
p_10 = t_1 * (1 + beta) * (alpha + phi) * p_00
p_01 = t_1 * ((1 + beta) / beta) * (alpha + 1 - phi) * p_00
p_busy = 1 - p_00 - (p_10 + p_01)
free_times = p_00 * T
busy_times = p_busy * T
print(f'Коэффициент использования: {alpha}')
print(f'А) Доля времени, когда оба продавца свободны: {free_times / 100:.1f}%\n\
Доля времени, когда оба продавца заняты: {busy_times / 100:.1f}%\n')
print(f'Вероятность того, что оба продавца свободны: {p_00}')

print(f'Б) Вероятность того, что первый продавец занят, а второй свободен: {p_10}')
print(f'Вероятность того, что второй продавец занят, а первый свободен: {p_01}')

print(f'Вероятность того, что оба продавца заняты = {p_busy}')

p_2 = (alpha ** 2 / (1 + 2 * alpha)) * ((1 + beta) / beta) * \
      (1 + (1 + beta) * alpha - (1 - beta) * phi) * p_00
p_3 = (alpha ** 3 / (1 + 2 * alpha)) * ((1 + beta) / beta) * \
      (1 + (1 + beta) * alpha - (1 - beta) * phi) * p_00

p_m = 1 - (p_00 + p_01 + p_10 + p_2 + p_3)
print(f'В) Вероятность того, что в магазине больше 3 покупателей: {p_m}')

t_1 = alpha * (1 + beta) / (1 - alpha)
t_2 = 1 + (1 + beta) * alpha - (1 - beta) * phi
t_3 = beta * (1 + 2 * alpha) + \
      alpha * (1 + (1 + beta ** 2) * alpha - (1 - beta ** 2) * phi)

n = t_1 * (t_2 / t_3)
print('Г) Среднее число покупателей в магазине:', n)

h = (p_01 + p_10) + 2 * p_busy
b = n - h
w = b / lmbd
print('Д) Среднее время ожидания покупателя в очереди:', w)

u = n / lmbd
print('Е) Среднее время пребывания покупателя в магазине:', u)
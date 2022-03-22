# M/M(k, k)/1

import matplotlib.pyplot as plt
from sympy import solve
from sympy.abc import x

k = 3
lambda_ = 1 / 5
mu = 1 / 10
ticket_price = 50
cost = 170
time = 9

psi = lambda_ / (k * mu)

def get_r(equation, pow):
    s = solve(equation)
    # print(s)
    return s[0] if pow % 2 != 0 else s[1]

r = get_r(x + x ** 2 + x ** 3 - (lambda_ / mu), k)

print('r = ', r)
print('Check: ', lambda_ / mu, ' = ', sum([r ** i for i in range(1, k + 1)]))

def get_p_0(_r, _k):
    return (1 - _r) / _k

def get_p_q(_r, _k, _q):
    return (1 - _r ** (_q + 1)) / _k

def get_p_kn(_r, _psi, _n):
    return _psi * (1 - _r) * (_r ** _n)

# а) среднее время ожидания в очереди
p_0 = get_p_0(r, k)
tmp_1 = p_0 / (1 - r)
tmp_2 = (k * (k - 1)) / 2
tmp_3 = (r ** 2 * (k * r ** (k - 1) * (1 - r) - (1 - r ** k))) / ((1 - r) ** 2)
tmp_4 = p_0 * (1 - r ** k) / (1 - r)
tmp_5 = (r ** 2) / ((1 - r) ** 2)
b = tmp_1 * (tmp_2 + tmp_3) + tmp_4 * tmp_5

w = b / lambda_
print('A) Среднее время ожидания в очереди:', w)

# б) вероятность того, что аттракцион простаивает
p_p = p_0 + sum([get_p_q(r, k, q) for q in range(1, k)])
print('Б) Вероятность того, что аттракцион простаивает:', p_p)

# в) среднее число человек, ожидающих в очереди 
print('В) Среднее число человек, ожидающих в очереди:', b)

# г) вероятность ожидания в очереди 
p_wait_q = sum([get_p_q(r, k, q) for q in range(1, k)]) + sum([get_p_kn(r, psi, n) for n in range(500)])
p_wait_q = 1 - get_p_q(r, k, k - 1)
print('Г) Вероятность ожидания в очереди:', p_wait_q)

# д) долю времени, в течение которого аттракцион используется 
p_w = 1 - p_p
print('Д) Долю времени, в течение которого аттракцион используется:', p_w)

# е) средние значения выручки и прибыли от использования аттракциона
ans_1 = ticket_price * k * time * p_w * (60 / (1 / mu)) 
print('Е) Среднее значение выручки от использования аттракциона:', ans_1)

ans_2 = cost * time * p_w * (60 / (1 / mu))
print('   Среднее значение прибыли от использования аттракциона:', ans_1 - ans_2)

# Определить, как изменятся средняя прибыль и среднее время ожидания 
# в очереди при различных значениях вместимости аттракциона – от 3 до 10 человек
k_s = list(range(3, 11))
income = []
w_s = []

equation = x + x ** 2 - (lambda_ / mu)

for k_tmp in k_s:
    equation += x ** k_tmp
    r = get_r(equation, k_tmp)
    print('r =', r, ':', equation, '\n')
    
    p_0 = get_p_0(r, k_tmp)

    tmp_1 = p_0 / (1 - r)
    tmp_2 = (k_tmp * (k_tmp - 1)) / 2

    tmp_3 = r ** 2 * (k_tmp * r ** (k_tmp - 1) * (1 - r) - (1 - r ** k_tmp)) / (1 - r) ** 2

    tmp_4 = p_0 * (1 - r ** k_tmp) / (1 - r)
    tmp_5 = (r ** 2) / ((1 - r) ** 2)

    b = tmp_1 * (tmp_2 + tmp_3) + tmp_4 * tmp_5

    w = b / lambda_
    w_s.append(w)

    p_p = p_0 + sum([get_p_q(r, k_tmp, q) for q in range(1, k_tmp)])
    p_w = 1 - p_p

    ans_1 = ticket_price * k_tmp * time * p_w * (60 / (1 / mu)) 
    ans_2 = cost * time * p_w * (60 / (1 / mu))
    income.append(ans_1 - ans_2)
    
print(k_s)
print(income)
print(w_s)

plt.plot(k_s, income)
plt.title('Зависимость средней прибыли\nот вместимости аттракциона')
plt.xlabel('Вместимость аттракционов, чел.')
plt.ylabel('Средняя прибыль, ед.')
plt.show()

plt.plot(k_s, w_s)
plt.title('Зависимость среднего ожидания в очереди\nот вместимости аттракциона')
plt.xlabel('Вместимость аттракционов, чел')
plt.ylabel('t_wait, мин')
plt.show()
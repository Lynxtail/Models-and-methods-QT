from math import exp, factorial
import numpy as np

N = 2
lmbd = 2
v = 0.5
mu = 1 / v

# N = 3
# lmbd = 2/5
# v = 7
# mu = 1 / v

alpha = lmbd / mu
print(f'alpha: {alpha}')

def p_1(n):
    return ((alpha ** (n + 1) * sum([alpha ** i for i in range(N - n + 1)])) /
            (sum([alpha ** i for i in range(N + 1)]))) * p_0_0
    # return (alpha * sum([alpha ** (-i) for i in range(N - n + 1)])) / \
    # ((N+1) * exp(alpha) + sum([(N - i + 1) * alpha ** (-i) for i in range(1, N+1)]))


def pnk(k):
    return (alpha ** (k + N) / (factorial(k) * sum([alpha ** i for i in range(N + 1)]))) * p_0_0
    # return (alpha ** k / factorial(k)) / \
    #     ((N + 1) * exp(alpha) + sum([(N - i + 1) * alpha ** (-i) for i in range(1, N+1)]))

t_1 = sum([alpha ** (-i) for i in range(N + 1)])
t_2 = sum([(N - i + 1) * alpha ** (-i) for i in range(1, N + 1)])
p_1_0 = (alpha * t_1) / ((N + 1) * exp(alpha) + t_2)

p_0_0 = p_1_0 / alpha
print(f'А) Вероятность того, что у раздаточного окна инструментальной кладовой никого из рабочих нет, и дежурный \
кладовщик свободен от выдачи:  {p_0_0}')

p_1_1 = p_1(1)
p_1_2 = p_1(2)

# p_1_3 = p_1(3)

p = [[p_1_0],
    [p_1_1],
    [p_1_2]]
    # [p_1_3]]

for i in range(N + 1):
    for k in range(2, 8):
        p[i].append(pnk(k))

p = np.array(p)
p_k = [p.transpose()[k].sum() for k in range(7)]
print(f'\nБ) Вероятности того, что на раздаче инструмента будет занято 1, 2, 3, ..., 7 кладовщиков, при n = 0, 1, 2:\n')
for k in range(7):
    print(f'p({k + 1}, n) = {p_k[k]}')

# вероятности того, что очередь не будет превышать N человек при 
# условии, что на раздаче инструмента будет занято 1, 2, 3, ..., 7 кладовщиков
# \ p(1,0), p(2,0), p(3,0), p(4,0), p(5,0), p(6,0), p(7,0).
# \ p(1,1), p(2,1), p(3,1), p(4,1), p(5,1), p(6,1), p(7,1).
# \ p(1,2), p(2,2), p(3,2), p(4,2), p(5,2), p(6,2), p(7,2).

print()
for s in p:
    for item in s:
        print(f'{item:.5f}', end='; ')
    print()

print('\nВ) Вероятности того, что очередь не будет превышать N человек при условии, что на раздаче инструмента будет \
занято 1, 2, 3,..., 7 кладовщиков:\n')

p_N = []
for k in range(1, 8):
    res = p_0_0
    for n in range(N+1):
        res += pnk(k)
    p_N.append(res)
for k in range(1, 7):
    p_N[k] += sum([p[0][l] for l in range(k)])

[print(f"Вероятности того, что очередь не будет превышать 2 человек при условии, что на раздаче инструмента будет \
занято {k + 1} кладовщиков: {p_N[k]}") for k in range(len(p_N))]

print()
p_N = []

for k in range(7):
    res = p_0_0
    for n in range(N+1):
        res += p[n][k]
    p_N.append(res)
for k in range(1, 7):
    p_N[k] += sum([p[0][l] for l in range(k)])

[print(f"Вероятности того, что очередь не будет превышать 2 человек при условии, что на раздаче инструмента будет \
занято {k + 1} кладовщиков: {p_N[k]}") for k in range(len(p_N))]

print()
p_N = []

for k in range(7):
    res = p_0_0
    res += p_k[k]
    p_N.append(res)
for k in range(1, 7):
    p_N[k] += sum([p[0][l] for l in range(k)])
[print(f"Вероятности того, что очередь не будет превышать 2 человек при условии, что на раздаче инструмента будет \
занято {k + 1} кладовщиков: {p_N[k]}") for k in range(len(p_N))]

# среднее число занятых кладовщиков
h = sum([p_1(n) for n in range(N + 1)]) + \
     sum([k * sum([pnk(k) for _ in range(N + 1)]) for k in range(2, 100)])
print(f'Г) М.о. числа занятых кладовщиков: {h}')

# среднее число рабочих, ожидающих в очереди
# \ b
b = sum([n * p_1(n) for n in range(N + 1)]) + \
     sum([sum([n * pnk(k) for n in range(N + 1)]) for k in range(2, 100)])
print(f'Д) М.о. числа рабочих, ожидающих в очереди: {b}')

# среднее время пребывания рабочих в очереди в ожидании выдачи инструмента
# \ w = b / lmbd
w = b / lmbd
print(f'Е) М.о. времени пребывания рабочих в очереди: {w}')

# среднее число кладовщиков с условием
a = 95 / 100
s = p_0_0
k = 0
while s < a:
    # s += p_k[k]
    s += p_N[k]
    k += 1

print(f'В среднем необходимо {k+1} кладовщиков, чтобы обеспечить обслуживание рабочих в заданных условиях с гарантийной вероятностью не ниже {a}')
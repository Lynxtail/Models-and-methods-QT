from itertools import chain, permutations

def change_priority(priority):
    lmbd = [1, 2, .5, 1.1, 3]
    v = [.2, .1, .1, .15, .01]
    c = [5, 4, 3, 2, 1]
    for i in range(len(priority)):
        lmbd[i], lmbd[priority[i]-1] = lmbd[priority[i]-1], lmbd[i]
        v[i], v[priority[i]-1] = v[priority[i]-1], v[i]
        c[i], c[priority[i]-1] = c[priority[i]-1], c[i]
    return lmbd, v, c

def get_prop(n, lmbd, v, c):
    mu = [1 / v[i] for i in range(n)]
    v_2 = [6*v[i] ** 2 for i in range(n)]
    psi = [lmbd[i] / mu[i] for i in range(n)]
    s = 0
    R_N = []
    for i in range(n):
        s += psi[i]
        R_N.append(s)

    delta = [v_2[i] / (2 * v[i]) for i in range(n)]
    sigma = []
    s = 0
    for i in range(n):
        s += psi[i] * delta[i]
        sigma.append(s)

    w = [sigma[0] / (1 - R_N[0])]
    for i in range(1, n):
        w.append(sigma[i] / ((1 - R_N[i - 1]) * (1 - R_N[i])))

    w_rand = sum([w[i] * lmbd[i] / sum(lmbd) for i in range(n)])

    F = sum([c[i] * lmbd[i] * w[i] for i in range(n)])

    # условия оптимизации абсолютных приоритетов
    cond1 = [c[i] / v[i] for i in range(n)]
    cond2 = [2 * v[i] * c[i] / v_2[i] for i in range(n)]
    flag = True
    for i in range(n):
        for j in range(n):
            if i > j and cond2[i] > cond1[j]:
                flag = False
                break
            elif i < j and cond2[i] < cond1[j]:
                flag = False
                break
    if cond1 == sorted(cond1) and flag:
        print('Оптимальный порядок приоритетов')
        [print(f'Коэффициент использования прибора (класс {i+1}): {R_N[i]:.1f}') for i in range(n)]
        [print(f'Средняя продолжительность ожидания обработки требований {i+1} класса: {w[i]:.1f}') for i in range(n)]
        print(f'Средняя продолжительность ожидания обработки требований из общего потока:\n{w_rand:.1f}')
        
        print('\tВторое условие\tПервое условие')
        [print(f'i = {i+1}:\t{round(cond2[i], 3)}\t\t{round(cond1[i], 3)}') for i in range(n)]
    else:
        # print('Неоптимальный порядок приоритетов')
        print(f'F: {F:.1f}')
        
if __name__ == '__main__':
    n = 5
    priorities = list(chain(permutations(range(1, n+1), n)))
    for i in range(len(priorities)):
        print(f'\nДля приоритетов: {priorities[i]}:\n')
        lmbd, v, c = change_priority((priorities[i]))
        get_prop(n, lmbd, v, c)

def get_prop_without_priorities(n, lmbd, v, c):
    mu = [1 / v[i] for i in range(n)]
    v_2 = [1.5*v[i] ** 2 for i in range(n)]
    psi = [lmbd[i] / mu[i] for i in range(n)]
    R_N = sum(psi)
    print(f'Коэффициент использования прибора (вне зависимости от класса требования): {R_N:.1f}')

    w = 0.5 * sum([v_2[i] * lmbd[i] for i in range(n)]) / (1 - R_N)
    print(f'Средняя продолжительность ожидания в каждой очереди: {w:.1f}')
    print(f'Среднее время ожидания произвольного заказа на обслуживание: {w:.1f}')

    F = sum([lmbd[i] * w * c[i] for i in range(n)]) + sum([c[i]*psi[i] for i in range(n)])
    print(f'\nF = {F:.1f}\n')

def get_prop_priorities(n, lmbd, v, c):
    mu = [1 / v[i] for i in range(n)]
    
    v_2 = [1.5*v[i] ** 2 for i in range(n)]
    
    psi = [lmbd[i] / mu[i] for i in range(n)]
    s = 0
    R_N = []
    for i in range(n):
        s += psi[i]
        R_N.append(s)
    [print(f'Коэффициент использования прибора (класс {i+1}): {R_N[i]:.1f}') for i in range(n)]

    w = [0.5 * sum([v_2[i] * lmbd[i] for i in range(n)]) / (1-R_N[0])]
    for j in range(1, n):
        w.append(0.5 * sum([v_2[i] * lmbd[i] for i in range(n)]) / ((1 - R_N[j-1])*(1-R_N[j])))

    [print(f'Средняя продолжительность ожидания в {j + 1}ой очереди: {w[j]:.1f}') for j in range(len(w))]

    w_rand = sum([w[i] * lmbd[i] / sum(lmbd) for i in range(n)])
    print(f'Среднее время ожидания произвольного заказа на обслуживание: {w_rand}')

    F = sum([lmbd[i] * w[i] * c[i] for i in range(n)]) + sum([c[i]*psi[i] for i in range(n)])
    print(f'\nF = {F:.1f}\n')

    [print(f'c[{i+1}]/v[{i+1}] = {c[i]/v[i]}') for i in range(n)]

def get_prop_abs(n, lmbd, v, c):
    mu = [1 / v[i] for i in range(n)]
    v_2 = [1.5*v[i] ** 2 for i in range(n)]
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
    
    [print(f'Коэффициент использования прибора (класс {i+1}): {R_N[i]:.1f}') for i in range(n)]
    [print(f'Средняя продолжительность ожидания обработки требований {i+1} класса: {w[i]:.1f}') for i in range(n)]
    print(f'Средняя продолжительность ожидания обработки требований из общего потока:\n{w_rand:.1f}')
    
    print(f'F: {F:.1f}')
    print('\tВторое условие\tПервое условие')
    [print(f'i = {i+1}:\t{round(cond2[i], 3)}\t\t{round(cond1[i], 3)}') for i in range(n)]
    
if __name__ == '__main__':
    n = 5
    
    # 1 2 3 4 5
    lmbd = [1, 2, .5, 1.1, 3]
    v = [.2, .1, .1, .15, .01]
    c = [5, 4, 3, 2, 1]
    print('_'*10)
    print('1 2 3 4 5')
    get_prop_abs(n, lmbd, v, c)

    # 5 2 3 1 4
    lmbd = [3, 2, .5, 1, 1.1]
    v = [.01, .1, .1, .2, .15]
    c = [1, 4, 3, 5, 2]
    print('_'*10)
    print('5 2 3 1 4')
    get_prop_abs(n, lmbd, v, c)

    # 1 2 3 4 5
    lmbd = [1, 2, .5, 1.1, 3]
    v = [.2, .1, .1, .15, .01]
    c = [5, 4, 3, 2, 1]
    print('_'*10)
    print('1 2 3 4 5')
    get_prop_priorities(n, lmbd, v, c)

    # 5 2 3 1 4
    lmbd = [3, 2, .5, 1, 1.1]
    v = [.01, .1, .1, .2, .15]
    c = [1, 4, 3, 5, 2]
    print('_'*10)
    print('5 2 3 1 4')
    get_prop_priorities(n, lmbd, v, c)

    # 1 2 3 4 5
    lmbd = [1, 2, .5, 1.1, 3]
    v = [.2, .1, .1, .15, .01]
    c = [5, 4, 3, 2, 1]
    print('_'*10)
    print('1 2 3 4 5')
    get_prop_without_priorities(n, lmbd, v, c)
    



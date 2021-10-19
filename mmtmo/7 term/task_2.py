from itertools import chain, permutations

def change_priority(priority):
    lmbd = [.2, .3, .1]
    v = [2., 1., 2.]
    c = [3., 2., 1.]
    for i in range(len(priority)):
        lmbd[i], lmbd[priority[i]-1] = lmbd[priority[i]-1], lmbd[i]
        v[i], v[priority[i]-1] = v[priority[i]-1], v[i]
        c[i], c[priority[i]-1] = c[priority[i]-1], c[i]
    return lmbd, v, c

def get_prop(n, lmbd, v, c):
    d = .5
    mu = [1 / v[i] for i in range(n)]
    v_2 = [d + v[i] ** 2 for i in range(n)]
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


    w_rand = 0.5 * sum([v_2[i] * lmbd[i] for i in range(n)]) / (1 - R_N[-1])
    print(f'Среднее время ожидания произвольного заказа на обслуживание: {w_rand:.1f}')

    w_rand = sum([w[i] * lmbd[i] / sum(lmbd) for i in range(n)])
    print(f'Среднее время ожидания произвольного заказа на обслуживание: {w_rand}')


    b = [lmbd[i] * w[i] for i in range(len(lmbd))]
    [print(f'Среднее число заказов в {i + 1} очереди: {b[i]:.1f}') for i in range(len(b))]
    print(f'Средняя длина очереди: {sum(b):.1f}')

    F = sum([lmbd[i] * w[i] * c[i] for i in range(n)]) + sum([c[i]*psi[i] for i in range(n)])
    print(f'\nF = {F:.1f}\n')

    flag = True
    for i in range(n-1):
        if c[i]/v[i] < c[i+1]/v[i+1]:
            print('Неоптимальный порядок расстановки приоритетов:')
            flag = False
            break 
        elif i == n-2:
            print('Оптимальный порядок расстановки приоритетов:')

    [print(f'c[{i+1}]/v[{i+1}] = {c[i]/v[i]}') for i in range(n)]
    print('_'*50)
    # return flag

if __name__ == "__main__":
    n = 3
    lmbd, v, c = change_priority([1, 2, 3])
    priorities = list(chain(permutations(range(1, n+1), n)))
    print(priorities, '\n')

    for i in range(len(priorities)):
        print(f'\nДля приоритетов: {priorities[i]}:\n')
        lmbd, v, c = change_priority((priorities[i]))
        get_prop(n, lmbd, v, c)
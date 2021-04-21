import numpy as np
import matplotlib.pyplot as plt


def expected_n(lmbd, mu):
    return lmbd / (mu - lmbd)


def expected_u(lmbd, mu):
    return 1 / (mu - lmbd)


def stationary_distribution(omega, theta, eps):
    while np.linalg.norm(omega.dot(theta) - omega) > eps:
        omega = omega.dot(theta)
    return omega


def get_lmbds(lmbd_0, omega):
    ans = [lmbd_0 * omega[1] / omega[0]]
    for i in range(2, L + 1):
        ans.append(ans[-1] * omega[i] / omega[0])
    return ans


L = 7
# kappa = [1, 1, 2, 1, 4, 2, 3]
kappa = [1] * L
mu = [140, 65, 90, 143, 160, 184, 183]
theta = np.array([[0, 0.3, 0, 0.08, 0.02, 0.3, 0.3, 0],
                  [0, 0, 0.5, 0, 0, 0.2, 0.3, 0],
                  [0.4, 0.3, 0, 0, 0.2, 0, 0.1, 0],
                  [0, 0.8, 0, 0, 0.01, 0, 0.14, 0.05],
                  [0.4, 0, 0, 0.1, 0, 0.2, 0.3, 0],
                  [0, 0, 0.1, 0.1, 0, 0, 0.5, 0.3],
                  [0, 0, 0, 0.9, 0.1, 0, 0, 0],
                  [0, 0, 0, 0.6, 0.2, 0, 0.1, 0.1]])

# нахождение вектора omega
omega = np.array([0.3, 0.4, 0, 0, 0, 0.3, 0, 0])
eps = 0.0001
omega = stationary_distribution(omega, theta, eps)
print(f'Omegas: {omega},\nCheck (~1): {sum(omega)}')

# изменение параметров

lmbds_to_plot = np.linspace(0.1, 4, 20)
n_s_s = []
u_s_s = []
for lmbd_0 in lmbds_to_plot:
    lmbds = get_lmbds(lmbd_0, omega)
    n_s = np.array([expected_n(lmbds[i], mu[i]) for i in range(L)])
    u_s = np.array([expected_u(lmbds[i], mu[i]) for i in range(L)])
    n_s_s.append(n_s)
    u_s_s.append(u_s)
    print(f'\nlambda_0: {lmbd_0}\nN: {n_s},\nU: {u_s}')
n_s_s = np.array(n_s_s)
u_s_s = np.array(u_s_s)
n_s_s = np.transpose(n_s_s)
u_s_s = np.transpose(u_s_s)
for i in range(len(n_s_s)):
    plt.figure(1)
    plt.plot(lmbds_to_plot, n_s_s[i], 'o-', label=f'System {str(i + 1)}')
    plt.suptitle(
        f'Зависимость мат. ожидания числа требований\nв системах от интенсивности поступающих в сеть требований')
    plt.legend()
    plt.figure(2)
    plt.plot(lmbds_to_plot, u_s_s[i], 'o-', label=f'System {str(i + 1)}')
    plt.suptitle(
        f'Зависимость мат. ожидания длительностей пребывания требований\nв системах от интенсивности поступающих в сеть требований')
    plt.legend()

mu_to_plot = np.linspace(100, 200, 20)
n_s_s = []
u_s_s = []
lmbd_0 = 4
for mu_4 in mu_to_plot:
    lmbds = get_lmbds(lmbd_0, omega)
    mu[3] = mu_4
    n_s = np.array([expected_n(lmbds[i], mu[i]) for i in range(L)])
    u_s = np.array([expected_u(lmbds[i], mu[i]) for i in range(L)])
    n_s_s.append(n_s)
    u_s_s.append(u_s)
    print(f'\nmu_4: {mu_4}\nN: {n_s},\nU: {u_s}')
n_s_s = np.array(n_s_s)
u_s_s = np.array(u_s_s)
n_s_s = np.transpose(n_s_s)
u_s_s = np.transpose(u_s_s)
for i in range(len(n_s_s)):
    plt.figure(3)
    plt.plot(mu_to_plot, n_s_s[i], 'o-', label=f'System {str(i + 1)}')
    plt.suptitle(
        f'Зависимость мат. ожидания числа требований\nв системах от интенсивности обслуживания в 4-й системе')
    plt.legend()
    plt.figure(4)
    plt.plot(mu_to_plot, u_s_s[i], 'o-', label=f'System {str(i + 1)}')
    plt.suptitle(
        f'Зависимость мат. ожидания длительностей пребывания требований\nв системах от интенсивности обслуживания в 4-й системе')
    plt.legend()
plt.show()

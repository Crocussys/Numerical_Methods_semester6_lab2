import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math


def f(x):
    return math.log(x) + x ** 2 - 8


def df(x):
    return 1 / x + 2 * x


def d2f(x):
    return 2 - 1 / x ** 2


def fi(x):
    return math.sqrt(8 - math.log(x))


def bisections(func, bounds, eps=1e-3):
    print("Метод бисекций")
    a, b = bounds
    print(f"[{a}, {b}]")
    fa, fb = func(a), func(b)
    print(f"f(a) = {fa}\nf(b) = {fb}", end="\n\n")
    if fa * fb > 0:
        print('На заданном интервале нет корней!')
        return
    x0 = (a + b) / 2
    ps = [x0]
    err = abs(b - a)
    i = 0
    while err >= eps:
        print(f"x{i} = {x0}")
        fxi = func(x0)
        print(f"f(x{i}) = {fxi}")
        i += 1
        if func(a) * fxi > 0:
            a = x0
        else:
            b = x0
        print(f"[{a}, {b}]")
        x0 = (a + b) / 2
        ps.append(x0)
        err = abs(b - a)
        print(f"|b - a| = {err}", end="\n\n")
    return ps


def newton(func, fprime, fprime2, bounds, eps=1e-3):
    print("Метод Ньютона")
    a, b = bounds
    if func(a) * fprime2(a) > 0:
        x0 = a
    elif func(b) * fprime2(b) > 0:
        x0 = b
    else:
        print('Неверно выбран начальный интревал!')
        return
    print(f"x0 = {x0}")
    x = x0 - func(x0) / fprime(x0)
    print(f"x1 = {x}")
    ps = [x0, x]
    i = 1
    err = abs(x - x0)
    print(f"|x{i} - x{i - 1}| = {err}")
    while err >= eps:
        i += 1
        x0 = x - func(x) / fprime(x)
        x = x0 - func(x0) / fprime(x0)
        print(f"x{i} = {x}")
        ps.append(x)
        err = abs(x - x0)
        print(f"|x{i} - x{i - 1}| = {err}")
    return ps


def secant(func, x0, x1, eps=1e-3):
    print("Метод секущих")
    x_prev, x = x0, x1
    print(f"x0 = {x0}")
    print(f"x1 = {x1}")
    ps = [x0, x1]
    i = 1
    err = abs(x - x_prev)
    print(f"|x{i} - x{i - 1}| = {err}")
    while err >= eps:
        i += 1
        x, x_prev = x - func(x) * (x - x_prev) / (func(x) - func(x_prev)), x
        print(f"x{i} = {x}")
        ps.append(x)
        err = abs(x - x_prev)
        print(f"|x{i} - x{i - 1}| = {err}")
    return ps


def iterations(phi, a, eps=1e-3):
    print("Метод простых итераций")
    i = 1
    x = phi(a)
    print(f"x0 = {x}")
    x0 = phi(x)
    print(f"x1 = {x0}")
    ps = [x0]
    err = abs(x - x0)
    print(f"|x{i - 1} - x{i}| = {err}")
    while err >= eps:
        x = phi(x0)
        x0 = phi(x)
        ps.append(x0)
        i += 1
        print(f"x{i} = {x}")
        err = abs(x - x0)
        print(f"|x{i - 1} - x{i}| = {err}")
        if i == 10000:
            print('Выполнено 10000 итераций, решение не нейдено!')
            return
    return ps


def chart(ps=None, title="", err=0.01):
    fig, ax = plt.subplots()
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.01))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.grid(which='major', color='gray')
    ax.grid(which='minor', color='gray', linestyle=':')
    plt.title(title, fontsize=18)
    plt.xlabel("x", fontsize=18)
    plt.ylabel("f(x)", fontsize=18)
    xs = [i * err for i in range(int(segment[0] / err), int(segment[1] / err) + 1)]
    ax.plot(xs, [0 for _ in range(len(xs))], color="black")
    ax.plot(xs, list(map(f, xs)), label="Исходная функция")
    if ps is not None:
        ax.scatter(ps[:-1], [0 for _ in range(len(ps) - 1)], color="green", label="Итерации")
        ax.scatter(ps[-1], 0, color="red", label="Решение")
        print(f"Ответ: {ps[-1]}")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    segment = (2, 3)
    chart()
    chart(bisections(f, (2, 3)), "Метод бисекций (метод деления отрезка пополам)")
    chart(newton(f, df, d2f, (2, 3)), "Метод Ньютона (метод касательных)")
    chart(secant(f, 2, 3), "Метод секущих (метод хорд)")
    chart(iterations(fi, 2), "Метод простых итераций")

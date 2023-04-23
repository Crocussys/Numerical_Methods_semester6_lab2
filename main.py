import math


def f(x):
    return math.log(x) + x ** 2 - 8


def df(x):
    return 1 / x + 2 * x


def d2f(x):
    return 2 - 1 / x ** 2


def fi(x):
    return math.sqrt(8 - math.log(x))


def bisections(func, bounds, eps=1e-4):
    a, b = bounds
    if func(a) * func(b) > 0:
        print('На заданном интервале нет корней!')
        return
    x0 = (a + b) / 2
    while abs(a - b) >= eps:
        if func(a) * func(x0) > 0:
            a = x0
        else:
            b = x0
        x0 = (a + b) / 2
    return x0


def newton(func, fprime, fprime2, bounds, eps=1e-4):
    a, b = bounds
    if func(a) * fprime2(a) > 0:
        x0 = a
    elif func(b) * fprime2(b) > 0:
        x0 = b
    else:
        print('Неверно выбран начальный интревал!')
        return
    x = x0 - func(x0) / fprime(x0)
    while abs(x - x0) >= eps:
        x0 = x - func(x) / fprime(x)
        x = x0 - func(x0) / fprime(x0)
    return x


def secant(func, x0, x1, eps=1e-4):
    x_prev, x = x0, x1
    while abs(x - x_prev) >= eps:
        x, x_prev = x - func(x) * (x - x_prev) / (func(x) - func(x_prev)), x
    return x


def iterations(phi, a, eps=1e-4):
    i = 1
    x = phi(a)
    x0 = phi(x)
    while abs(x - x0) >= eps:
        x = phi(x0)
        x0 = phi(x)
        i += 1
        if i == 10000:
            print('Выполнено 10000 итераций, решение не нейдено!')
            return
    return x0


if __name__ == '__main__':
    print(bisections(f, (2, 3)))
    print(newton(f, df, d2f, (2, 3)))
    print(secant(f, 2, 3))
    print(iterations(fi, 2))

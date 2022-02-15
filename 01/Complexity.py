def f1(n):
    """vypise n^2 hviezdiciek"""
    for i in range(n):
        for j in range(n):
            print('*')


def f2(n):
    """vypise (n^2 + n)/2 hviezdiciek"""
    for i in range(n):
        for j in range(i, n):
            print('*')


def f3(n):
    """vypise log_2(n) hviezdiciek"""

    # i=n --> i=n/2 --> i=n/4 --> i=n/8 --> ... --> i = n/(2^j)
    # n/(2^j) = 1 <-> n = 2^j <-> log_2(n) = j

    i = n

    while i >= 1:
        print('*')
        i = i//2


def f4(n):
    """vypise <= 2n hviezdiciek"""
    i = n

    while i > 0:
        if i % 2 == 1:
            for j in range(i):
                print("+")
        i = i//2

    # n=10 --> i=10 & 10*'+' --> i=5 & 5*'+' --> 2+ --> 1+ -->
    # n*'+' --> n/2 * '+' --> ... --> n/(2^j) * '+' --> '+'
    # n + n/2 + n/4 + ... + n/2^k + ... = n*(1 + 1/2 + 1/4 + 1/8 + ...) = 2n
    # 1 + 1/2 + 1/4 + 1/8 + ... = 2

    # O(f(n)) = {g:N-->N: EXISTUJE c, n_0 PRIRODZENE CISLO, ze PRE KAZDE n>n_0 g(n)<c*f(n)}

    # log(n)<c*2n (plati)

    # n < c*log(n) (neplati pre ziadne c)

    # f1 patri do O(f2) --> c=42 --> n^2 < 42*(n^2 + n)/2 <--> 0 < 40n^2 + 42n

    # f2 patri do O(f1) --> c=2, n_0=0 --> (n^2 + n)/2 < 2*n^2 <--> n^2 + n < 4n^2 <--> 0 < 3n^2 - n

    # O(f(n)) = O(c*f(n))


def najdimaximum(pole):
    max1 = pole[0]

    for i in pole:
        if i >= max1:
            max1 = i

    print(max1)


def najdimaxvusporiadanompoli(pole):
    print(pole[len(pole)-1])


# 2n+2 O(n)

# n^2 + h(n)
# h patri do O(n^2)

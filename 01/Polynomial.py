from itertools import zip_longest


class Polynomial:

    def __init__(self, *coefficients):
        """
        Class to work with polynomials.

        @coefficients: Coefficients are in the form a_n, ...a_1, a_0.
        """
        self.coefficients = list(coefficients)

    def evaluate(self, x):
        """
        Evaluate the polynomial at point x.

        @x: The number where to evaluate our polynomial.
        """
        res = 0
        for coeff in self.coefficients:
            res = res * x + coeff
        return res

    def string(self):
        """Returns a "nice" string representation of self."""
        exponent = self.degree()
        polynomial_string = ''

        for i in self.coefficients:
            polynomial_string += f'({i})x^{exponent} + '
            exponent -= 1

        return polynomial_string[:-3]

    def degree(self):
        """ Returns the degree of the polynomial. """
        return len(self.coefficients)-1

    def add(self, other):
        """Addition of this polynomial and an other.

        @other: The other summand.
        """
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]

        return Polynomial(*res)


p = Polynomial(1, -1, -1)
q = Polynomial(1, 2, 3)
r = p.add(q)


print(p.string())
print(q.string())
print(r.string())

# if 'var' is a decimal number then f'{var:.3f}' prints out the value of the decimal number 'var' truncated  to 3 decimal places
print(f'{p.evaluate(1.618):.5f}')

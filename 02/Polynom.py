class Polynom:
    
    def __init__(self, koeficienty):
        self.koeficienty = koeficienty

    def stupen(self):
        return len(self.koeficienty)-1

    def __len__(self):
        """
        Metoda, ktora vrati pocet koeficientov v self.
        """
        return self.stupen()+1

    def __str__(self):
        exponent = self.stupen()
        polynomial_string = ''

        for i in self.koeficienty:
            polynomial_string += f'({i})x^{exponent} + '
            exponent -= 1

        return polynomial_string[:-3]

class KvadratickyPolynom(Polynom):

    def __init__(self, koeficienty):
        super().__init__(koeficienty)
        if len(koeficienty) > 3:
            raise ValueError('toto nie je kvadraticky polynom')

    
    def __str__(self):
        return 'som kvadraticky'

    def ma_realny_koren(self):
        a = self.koeficienty[0]
        b = self.koeficienty[1]
        c = self.koeficienty[2]
        if b**2-4*(a*c) >= 0:
            return True
        else:
            return False



p = KvadratickyPolynom([1000,3,1])

q = KvadratickyPolynom([1,-1,-1])

print(p.ma_realny_koren())
print(q.ma_realny_koren())

print(q)
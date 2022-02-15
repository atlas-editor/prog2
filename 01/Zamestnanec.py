class Zamestnanec:

    def __init__(self, meno, vek, pozicia, plat):
        """
        Konstruktor pre zamestnanca

        @meno: Meno zamestnanca.
        @vek: Vek zamestnanca.
        @pozicia: Pozicia zamestnanca vo firme.
        @plat: Plat zamestnanca.
        """
        # deklarovanie instancnej premennej s nazvom 'x' a hodnotou 'y' sa v Pythone zapise ako:
        # self.x = y
        # instancne premenne sa deklaruju v konstruktore triedy, tj. v tele funkcie '__init__'
        self.meno = meno

        # v konstruktore mozeme kontrolovat vstupne hodnoty a nedovolit vytvorit akykolvek objekt
        if vek < 18:
            raise Exception("nemoze pracovat")

        self.vek = vek
        self.pozicia = pozicia
        self.plat = plat

    def zvys_plat(self, suma):
        """
        Metoda na zvysenie platu zamestnanca
        
        @suma: Novy plat zamestnanca.
        """

        if suma <= self.plat:
            # ak novy plat zamestnanca ma byt nizsi alebo rovny ako doterajsi tak upozornime uzivatela
            print('to nie je navysenie platu!')
        else:
            # v opacnom pripade jeho plat zmenime a vypise o tom info do konzoly
            self.plat = suma
            print(f'plat zamestnanca {self.meno} sa navysil na {self.plat}')

    def vyhod(ja, dovod):
        """
        Metoda na vyhodenie zamestnanca

        @dovod: Dovod terminacie.
        """
        print(f'vyhadzujeme zamestnanca {ja.meno}, pretoze {dovod}')


# vytvorenie noveho objektu triedy 'Zamestnanec'
david = Zamestnanec('David', 37, 'cviciaci', 1000)

# vypiseme meno a plat zamestnanca ulozeneho v premennej 'david' pomocou prisupu k instancnym premennym 'david.meno' a 'david.plat'
print(f'plat zamestnanca {david.meno} je: {david.plat}')

# volanie metody na zvysenie platu
# kedze novy plat je nizsi ako povodny plat sa nezmeni, ale informuje sa uzivatel vypisanim do konzoly
david.zvys_plat(900)

print(f'plat zamestnanca {david.meno} je: {david.plat}')

# volanie metody vyhod
david.vyhod('zle vysvetluje')

# Programování 2 - NMIN112

**Cvičiaci:** David Uhrik

**Výuka:** Ut 9:00 - 10:30 + 10:40 - 12:10, N10 (IMPAKT)

**E-mail:** uhrik@karlin.mff.cuni.cz

---

**Známkovanie:**
* praktické domáce úlohy (70% z N-1 najlepších výsledkov z N zadaní)
* teoretické domáce úlohy (70% z M-1 najlepších výsledkov z M zadaní)
* zápočtový program s dokumentáciou
* zápočet (70%)

**Absencie:** Účasť na cvičení povinná nie je, ale v prípade _aktívnej_ účasti budem udeľovať bonusové body.

**Vypracovanie domácich úloh:** Kooperácia pri riešení domácich úloh je vítana, avšak očakáva sa, že svoje riešenia si píšete individuálne. Teda priame prepisovanie je zakázané a mali by ste pochopiť riešenie úlohy dostatočne, aby ste si vedeli napisať vlastné riešenie.

**TeX:** Ak by ste mali záujem vypracovať svoje riešenia k teoretickým domácim úlohám v systéme [$`\TeX`$](https://en.wikipedia.org/wiki/TeX), tak vam pomôže [táto stránka](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes) a môžete využiť [túto šablónu](https://www.overleaf.com/read/pcztzvcjycbj) na domáce úlohy.

---

[**Výsledky praktických domácich úloh**](practical_hw.md)

[**Výsledky teoretických domácich úloh**](theoretical_hw.md)

---

**Referencie:**
* [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
* [Mark Pilgrim - Dive Into Python 3](https://diveintopython3.net/index.html)
* [Mark Pilgrim - Ponořme se do Pythonu 3](http://diveintopython3.py.cz/index.html)
* [Martin Mareš, Tomáš Valla - Průvodce labyrintem algoritmů](http://pruvodce.ucw.cz/)
* Pavel Töpfer -  Algoritmy a programovací techniky
* Zed A. Shaw - Learn Python 3 the Hard Way
* Zed A. Shaw - Learn More Python 3 the Hard Way

---

## 15.2. - 21.2.

* **praktická časť:** Opakovanie základov Python-u: základné typy(`int`, `string`, `list`), práca s nimi; `for` cykly, `while` cykly, `if-else` konštrukty, typ `dict`, funkcie; triedy. Pozri kapitoly 1. až 5. a 9. v [[Py]](https://docs.python.org/3/tutorial/index.html). Alebo stručnejšie v kapitolách 1. až 4. a 7. v [[P]](https://diveintopython3.net/index.html); pozri taktiež súbor [`Zamestnanec.py`](01/Zamestnanec.py), tento príklad triedy sme si uvádzali na cvičení, ďalšie príklady tried sú: [`Laptop.py`](01/Laptop.py) alebo [`Polynomial.py`](01/Polynomial.py).

    * zadanie prvej praktickej domácej úlohy nájdete [tu](01/PHW1.md) a taktiež v ReCodEx-e, kam aj posielajte riešenia, v prípade otázok a nejasností ma neváhajte kontaktovať


* **teoretická časť:** Časová zložitosť programov a ich vyhodnotenie a porovnávanie. Pozri sekcie 2.2 až 2.4 v [[MV]](http://pruvodce.ucw.cz/); v súbore [`Complexity.py`](01/Complexity.py) nájdete sylabus cvičenia, ale v sekciách 2.2 až 2.4 nájdete to isté, ale lepšie a podrobnejšie popísané.

---

## 22.2. - 28.2.

* **praktická časť:** Pokračovanie úvodu do tried v Python (magické metódy, podtriedy, ...). Pozri kapitolu 9. v [[Py]](https://docs.python.org/3/tutorial/index.html) ďalej kapitolu 7. v [[P]](https://diveintopython3.net/index.html) a/alebo prednášku z 1.12. od [Martina Mareša](http://mj.ucw.cz/vyuka/2021/p1m/), pozri taktiež súbory z minula: [`Zamestnanec.py`](01/Zamestnanec.py), [`Laptop.py`](01/Laptop.py) a [`Polynomial.py`](01/Polynomial.py); súbor na ktorom sme pracovali tento týždeň, je: [`Polynom.py`](02/Polynom.py)

    * zadanie druhej praktickej domácej úlohy je v priečinku `02`: [`PHW2.md`](02/PHW2.md) a taktiež v ReCodEx-e. Dealine: `1.3.2022 9:00`

* **teoretická časť:** $`O`$-notácia, časová zložitosť programov a ich vyhodnotenie a porovnávanie, použitie pojmu limity pri porovnaní časovej zložitosti. Pozri sekcie 2.2 až 2.4 v [[MV]](http://pruvodce.ucw.cz/)

    * zadanie prvej teoretickej domácej úlohy je v priečinku `02`: [`THW1.md`](02/THW1.md) a taktiež v ReCodEx-e. Úlohy mi môžete priniesť aj na najbližie cvičenie alebo na cvičenie o dva týždne alebo aj poslať mailom. Dealine: `8.3.2022 9:00`

---

## 1.3. - 7.3.

* **praktická časť:** Precvičovanie niektorých významných algoritmov: Eratostenovo sito, Hornerovo schéma, binárne vyhľadávanie. Zdroje nájdete na [stránke doc. Töpfera](https://ksvi.mff.cuni.cz/~topfer/)

    * zadanie tretej praktickej domácej úlohy je v priečinku `03`: [`PHW3.md`](03/PHW3.md) a taktiež v ReCodEx-e. Dealine: `8.3.2022 9:00`

* **teoretická časť:** Návrh algoritmov na problémy typu: zisti, či postupnosť obsahuje dané číslo $`k`$; rozhodni, či postupnosť je monotónna; urči počet čísel bez opakovania v postupnosti; nájdi súvislý úsek v potupnosti s maximálnym súčtom. Pozri sekciu 1.1 v [[MV]](http://pruvodce.ucw.cz/)

---

## 8.3. - 14.3.

* **praktická časť:** Základy používania knižnice `numpy`. Návod na inštaláciu môžete nájsť [tu, v časti "6. CVIČENÍ"](https://ksvi.mff.cuni.cz/~peskova/index.php?p=vyuka_ls#programovani). Pozri taktiež [slidy](http://mj.ucw.cz/vyuka/2021/p2m/02-numpy.pdf) od Martina Mareša, resp. [videozáznam](https://kam.mff.cuni.cz/~mares/video/ls2021/p2m/02-numpy.mp4) z jeho cvičenia z roku 2021; dôležitý zdroj je taktiež [oficiálna dokumentácia](https://numpy.org/devdocs/user/) `numpy`; na cvičenie som veľa čerpal aj zo stránky [Real Python](https://realpython.com/numpy-tutorial/).

    * zadanie štvrtej praktickej domácej úlohy je tu: [`PHW4.md`](04/PHW4.md) a taktiež v ReCodEx-e. Dealine: `15.3.2022 9:00`

* **teoretická časť:** Precvičovanie triedacich algoritmov: Selection sort, Insertion sort, Shellsort, Bubble sort, Merge sort. Nájdenie všetkých výskytov daného čísla $`k`$ v usporiadanom poli pomocou binárneho hľadania. Video o "triedení tancom" nájdete [tu](https://www.youtube.com/watch?v=lyZQPjUT5B4) a na ich kanály nájdete aj implementovanie ďalších triediacich algoritmov do tanca.

    * zadanie druhej teoretickej domácej úlohy je tu: [`THW2.md`](04/THW2.md) a taktiež v ReCodEx-e. Úlohy mi môžete priniesť alebo aj poslať mailom. Dealine: `22.3.2022 9:00`

---

## 15.3. - 21.3.

TBA
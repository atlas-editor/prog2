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

**Zápočtový program:** Na úspešné zvládnutie cvičenia potrebujete vypracovať takzvaný "zápočtový program". Štandardne ide o netriviálny program (aplikáciu, knižnicu, ...) o rozsahu niekoľko stoviek radkov kódu ku ktorému potrebujete okrem samotného programu napísať uživateľskú dokumentáciu a programátorskú dokumentáciu. Súčasťou je aj "obhajoba" vašej práce, kde mi v krátkosti predvediete ako vaša aplikácia funguje (na termíne sa dohodneme individuálne). Postup pre vypracovanie programu:

1. vybrať téma a poslať krátky abstrakt mne na schválenie do **30.4.2022**
2. program aj s dokumentáciami poslať najneskôr do **31.8.2022**
3. v prípade nedostatkov vám dám program prepracovať

Ďalšie [info o zápočtovom programe nájdete na stránkach Mareša](http://mj.ucw.cz/vyuka/2021/p2m/zapoctaky.html), kde taktiež nájdete aj mnohé [námety](http://mj.ucw.cz/vyuka/zap/). K dokumentácií je vám k dispozícií pekne napísaný [text od Kryla](https://ksvi.mff.cuni.cz/~kryl/dokumentace.htm).

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
* [Steven S. Skiena - The Algorithm Design Manual](https://doc.lagout.org/science/0_Computer%20Science/2_Algorithms/The%20Algorithm%20Design%20Manual%20%282nd%20ed.%29%20%5bSkiena%202008-07-26%5d.pdf)

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

* **praktická časť:** Základy typovania v Python, vývojové prostredie Visual Studio Code, debugging a pokračovanie úvodu do `numpy`, modul `numpy.linalg`, základy vykresľovania grafov v `matplotlib`. K typovaniu pozri napríklad článok v [Real Python](https://realpython.com/python-type-checking/) a taktiež [slidy](http://mj.ucw.cz/vyuka/2021/p2m/03-typing.pdf) od Martina Mareša, resp. [videozáznam](https://kam.mff.cuni.cz/~mares/video/ls2021/p2m/03-typing-pycharm.mp4) z jeho cvičenia z roku 2021. Všetko potrebné čo sa týka VSCode nájdete na [oficiálnej stánke](https://code.visualstudio.com/docs/languages/python), kde je aj krátky [návod používania Python vo VSCode](https://code.visualstudio.com/docs/python/python-tutorial), okrem iného je tam aj niečo o debugging-u. Na oficiálnej [stránke `numpy`](https://numpy.org/doc/stable/reference/routines.linalg.html) nájdete info o práci s maticami v `numpy` a všeobecne veci týkajúce sa lineárnej algebry. K `matplotlib` odporúčam znovu [prednášku Martina Mareša](http://kam.mff.cuni.cz/~mares/video/ls2021/p2m/04-matplotlib.mp4)

    * zadanie piatej praktickej domácej úlohy je tu: [`PHW5.md`](05/PHW5.md) a taktiež v ReCodEx-e. Dealine: `22.3.2022 9:00`

* **teoretická časť:** Precvičovanie a analýza triedacich algoritmov: Counting sort, Radix sort. Dátové štruktúry: Queue (Fronta), Stack (Zásobník), Heap (Halda). Použitie zásobníka na overenie správneho ozátvorkovania výrazu. Riešenie problému s mediánom pomocou haldy, viď [link](https://www.youtube.com/watch?v=VmogG01IjYc).

---

## 22.3. - 28.3.

* **praktická časť:** Práca so spájanými zoznamami, viď. súbor [linked_list.py](06/linked_list.py).

    * zadanie šiestej praktickej domácej úlohy je tu: [`PHW6.md`](06/PHW6.md) a taktiež v ReCodEx-e. Dealine: `29.3.2022 9:00`

* **teoretická časť:** Práca s haldou (Heap), jej vytváranie, Heapsort. Spájané zoznamy (Linked list) a práca s nimi: pridanie prvku na začiatok/koniec, pridanie prvku na daný index, odobratie prvku, otočenie zoznamu. Ako referencie si môžete pozrieť sekciu 4.2 v knihe Mareša a/alebo sekcie 3.1 a 4.3 v knihe: The Algorithm Design Manual, viď. referencie.

    * zadanie tretej teoretickej domácej úlohy je tu: [`THW3.md`](06/THW3.md) a taktiež v ReCodEx-e. Dealine: `5.4.2022 9:00`

---

## 29.3. - 4.4.

* **praktická časť:** Práca s obojsmernými spájanými zoznamami a rekurzívnymi metódami na nich, viď. súbor [dll.py](07/dll.py).

    * zadanie siedmej praktickej domácej úlohy je tu: [`PHW7.md`](07/PHW7.md) a taktiež v ReCodEx-e. Dealine: `5.4.2022 9:00`

* **teoretická časť:** Obojsmerné spájané zoznamy (Doubly linked list) a práca s nimi: pridanie prvku na začiatok/koniec, pridanie prvku na daný index, odobratie prvku. Rekurzia (nie len v programovaní); Fibonacciho postupnosť, Kochova krivka, strom volaní, call stack, stack frame. Ako referenciu si môžete pozrieť tento [krátky text](https://www.cs.cornell.edu/courses/cs4120/2016sp/lectures/lec_recursion_lists/) o rekurzií a spájaných zoznamoch.

* **zápočtový program:** viď. info vyššie

---

## 5.4. - 11.4.

TBD
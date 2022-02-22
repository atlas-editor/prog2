# Programming 2 &ndash; THW1

**1.1.** (1 point) Let $k,l$ be arbitrary non-zero natural numbers. Prove that $11k \cdot \log_{l+2}(n) \in \Theta (\log(n))$

---

**1.2.** (3 points) Sort the following functions in a way so that if $f$ precedes $g$, then $f \in O(g)$

* $n + 10^{10}$

* $2n^3 + 42n$

* $2^{n-3}$

* $14n + 99\log(n)$

* $n^3 \cdot \log^{10}(n)$

* $n!$

  In each case formally verify your claim.

---

**1.3.** (1 point) Prove that $O(f) = \{ g \in {}^\mathbf{N}\mathbf{N} : \limsup_{n \to \infty} \frac{f(n)}{g(n)} < \infty \}$.

---

**1.4.** (1 point) Find a tight asymptotic bound for the function $\log_n(n!)$.

---

**1.5.** (1 point) Find functions $f, g$ such that neither $f \in O(g)$ nor $g \in O(f)$.

---

**1.6.** (1 point) What is the time complexity of the following function:
```
def f(n):
    for i in range(n//2):
        j = 1
        while j + n//2 <= n:
            k = 1
            while k <= n:
                print('bmljZQo=')
                k *= 2
            j += 1
```

---

**1.7.** (1 point) What is the time complexity of the following function:
```
def g(n):
    for i in range(n):
        j = 1
        while j < n:
            print('ZGVjb2RpbmcK')
        j += i
```

---

**1.8.** (1 point) What is the time complexity of the following function:
```
def h(n):
    i = 0
    while i < n:
        j = n
        while j > 0:
            print('bWF0ZQo=')
            j //= 2
        i *= 2
```
# Programming 2 &ndash; PHW2

**2.1.** (10 points) Create a class `FrequencyTable` which is used to store the number of occurrences of words in a given text. You can think of a frequency table as a table that has $2$ columns: `word` and `number of occurrences` and every word occurs at most once in the table; for example:

---

| word  | number of occurrences |
| ----------------------- | ------------- |
| prog2  | 11  |
| math  | 17  |
| infinity | 1 |

---

Below is the structure of the class and your task is to implement the given methods as described in their docstrings.

```
class FrequencyTable:
    """
    A class to handle a frequency table.
    """

    def __init__(self):
        """
        The constructor: initializes an empty frequency table.
        """

        pass

    def clear(self):
        """
        Empties the contents of the frequency table.
        """

        pass

    def add_occurrence(self, s):
        """
        Adds an occurence of the word s into the frequency table.
        
        :param s: the word for which we want to add an occurrence into the frequency table
        """

        pass

    def remove_occurrence(self, s):
        """
        Removes an occurence of the word s from the frequency table, if s had frequency 1 then the entry for s should be removed from the table.
        
        :param s: the word whose frequency we want to decrease in the frequency table
        """

        pass

    def most_common(self):
        """
        Returns the word with the highest number of occurrences, if it is not unique return the lexicographically smallest.
        
        :returns: the lexicographically smallest most common word
        """

        pass

    def get_words(self):
        """
        Returns the set of all distinct words occurring in the frequency table (with number of occurences > 0).
        
        :returns: the set of distinct words in the frequency table
        """

        pass

    def __len__(self):
        """
        Returns the number of distinct words occurring in the frequency table (with number of occurences > 0).
        
        :returns: the number of distinct words in the frequency table
        """

        pass

    def __getitem__(self, s):
        """
        Returns the number of occurences of the word s in the frequency table.
        
        :param s: the word for which we need to return its frequency
        :returns: the frequency of the word s
        :raises KeyError: raises an exception when the word s is not present in the table
        """

        pass

    def __add__(self, other):
        """
        Merge two frequency tables into one.
        
        :returns: a new frequency table whose entries are pairs (s,i+k), where the word s has i occurences in self and k occurences in other
        """

        pass

    def __and__(self, other):
        """
        Returns the intersection of two frequency tables.
        
        :returns: a new frequency table whose entries are pairs (s,i), where the word s occurs in self with k many occurences and in other with l many occurences and i=min(k,l)
        """

        pass

    def __eq__(self, other):
        """
        Test whether two frequency tables have the same entries.
        
        :returns: True if self has exactly the same entries (words together with their occurrences) as other, False else
        """

        pass

    def __str__(self):
        """
        Returns a nice string representation of the frequency table.
        
        :returns: a string representation of the frequency table
        """

        pass

```

_Task_

Your task to implement the methods in the class `FrequencyTable` and upload it as `frequency_table.py`. Do not print anything into the console and do not rename the class name or any of the method names. You can, however, add helper methods into your implementation.

_Sample Usage_

```
>>> freq_table = FrequencyTable()
>>> freq_table.add_occurrence('continuum')
>>> freq_table.add_occurrence('continuum')
>>> freq_table['continuum']
2
>>> for i in range(3):
...     freq_table.add_occurrence('aleph0')
... 
>>> freq_table.most_common()
'aleph0'
>>> freq_table['aleph1']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "frequency_table.py", line 144, in __getitem__
    raise KeyError
KeyError
```

_Explanation_

Since the `__getitem__` magic method is implemented we can access the value of any word that is present in our table by calling `self[word]`, if `word` is not in the table `KeyError` is raised. Calling `self.most_common()` returns the word with the highest number of occurrences, in this case `continuum` has $2$ occurrences while `aleph0` has $3$.

---

***2.2.** (1 point) Atticus is taking Programming 2 and wants to solve every bonus problem on his homework. Unfortunately, statistics is not his strong suit and thus he is struggling with the following problem.

Given an array $X[]$ of size $n$ and a natural number $d$ calculate the number of indices $i$ such that $X[i]$ is at least two times larger than the median of the previous $d$-many numbers: $X[i-d], \ldots, X[i-1]$. Consider only indices $i$ which have at least $d$-many predecessors so you are able to calculate the median.

_Input Format_

The first line contains space separated integers $n$ and $d$. The second line contains the array $X[]$ of $n$ integers each separated by a space.

_Constraints_

* $1 \le n < 10^6$
* $1 \le d < n$
* $0 \le X[i] \le 200$

_Output Format_

Print the number of indices $i \ge d$ such that $X[i] \ge 2 \cdot \mathrm{median}(X[i-d], \ldots, X[i-1])$.

_Sample Input_

```
5 4
1 2 3 4 5
```

_Sample Output_

```
1
```

_Explanation_

As $d=4$ we only check the median condition for the last element of the list. The median of $1,2,3,4$ is $2.5$ and $5 \ge 2 \cdot 2.5$ so the condition is met once and we print $1$.
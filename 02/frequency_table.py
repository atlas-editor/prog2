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
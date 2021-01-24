
import itertools
import collections


class Levenstein:

    @staticmethod
    def usual(string1, string2):
        """
        >>> levenshtein_distance('AATZ', 'AAAZ')
        1
        >>> levenshtein_distance('AATZZZ', 'AAAZ')
        3
        """

        distance = 0

        if len(string1) < len(string2):
            string1, string2 = string2, string1

        for i, v in itertools.zip_longest(string1, string2, fillvalue='-'):
            if i != v:
                distance += 1
        return distance

    @staticmethod
    def deep(s1, s2, remove_desc = True):
        """
        Возвращается наименьшее расстояние левенштейна среди разных комбинаций case и с поправкой на скобки
        """
        if remove_desc and '(' in s2:
            s2 = s2[:s2.index('(')].rstrip()
        
        tmp = [
            Levenstein.usual(s1, s2),
            Levenstein.usual(s1.lower(), s2),
            Levenstein.usual(s1.upper(), s2),
            Levenstein.usual(s1.title(), s2)
            ]
        if ' ' in s1:
            tmp.append(Levenstein.usual(s1.capitalize(), s2))
        
        return min(tmp)



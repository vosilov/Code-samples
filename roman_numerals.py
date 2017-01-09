# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 13:59:01 2016

@author: Rustam
"""


def convert_to_roman(arabic_num):
    '''
    Converts an arabic numeral into roman numeral
    arabic_num: (integer) a number ranging from 1 to 3999
    Returns: a roman numeral as string
    '''
    if arabic_num > 3999 or arabic_num < 1:
        return 'Please, choose a number ranging from 1 to 3999'

    roman = ''

    def convert_by_digit(str_arabic_digit, i):
        '''
        Converts a single digit into a roman numeral.
        str_arabic_digit: (string) single digit arabic numeral
        i:                (integer) the position of the digit. Can be either
                          0, 1, 2 or 3.
        '''
        roman_digit = ''
        arabic_digit = int(str_arabic_digit)
        
        mapping = {'start': ['I', 'X', 'C', 'M'],
                   'middle': ['V', 'L', 'D'],
                   'end': ['X', 'C', 'M']}

        if arabic_digit == 0:
            return roman_digit
        elif arabic_digit < 5:
            if 5 - arabic_digit > 1:
                roman_digit = arabic_digit * mapping['start'][i]
            else:
                roman_digit = mapping['start'][i] + mapping['middle'][i]
        elif arabic_digit == 5:
            roman_digit = mapping['middle'][i]
        elif arabic_digit > 5:
            if 10 - arabic_digit > 1:
                roman_digit = mapping['middle'][i] + (arabic_digit - 5) * mapping['start'][i]
            else:
                roman_digit = mapping['start'][i] + mapping['end'][i]
        
        return roman_digit

    for i, digit in enumerate(str(arabic_num)):
        roman += convert_by_digit(digit, len(str(arabic_num)) - i - 1)

    return roman

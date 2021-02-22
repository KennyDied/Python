rule_add = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

rule_div = {
    ('I', 'V'): 3,
    ('I', 'X'): 8,
    ('X', 'L'): 30,
    ('X', 'C'): 80,
    ('C', 'D'): 300,
    ('C', 'M'): 800,
}

def roman_to_arabic(roman_number):
    number = 0
    prev_literal = None
    for literal in roman_number:
        if prev_literal and rule_add[prev_literal] < rule_add[literal]:
            number += rule_div[(prev_literal, literal)]
        else:
            number += rule_add[literal]
        prev_literal = literal
    return number



import unittest

class RomanNumTest(unittest.TestCase):
    def test_roman_num(self):
        self.assertEquals(roman_to_arabic('I'), 1)
        self.assertEquals(roman_to_arabic('II'), 2)
        self.assertEquals(roman_to_arabic('III'), 3)
        self.assertEquals(roman_to_arabic('IV'), 4)
        self.assertEquals(roman_to_arabic('V'), 5)
        self.assertEquals(roman_to_arabic('VI'), 6)
        self.assertEquals(roman_to_arabic('VII'), 7)
        self.assertEquals(roman_to_arabic('VIII'), 8)
        self.assertEquals(roman_to_arabic('IX'), 9)
        self.assertEquals(roman_to_arabic('X'), 10)
        self.assertEquals(roman_to_arabic('XXXI'), 31)
        self.assertEquals(roman_to_arabic('XLVI'), 46)
        self.assertEquals(roman_to_arabic('XCIX'), 99)
        self.assertEquals(roman_to_arabic('DLXXXIII'), 583)
        self.assertEquals(roman_to_arabic('DCCCLXXXVIII'), 888)
        self.assertEquals(roman_to_arabic('MDCLXVIII'), 1668)
        self.assertEquals(roman_to_arabic('MCMLXXXIX'), 1989)
        self.assertEquals(roman_to_arabic('MMX'), 2010)
        self.assertEquals(roman_to_arabic('MMXI'), 2011)
        self.assertEquals(roman_to_arabic('MMXII'), 2012)
        self.assertEquals(roman_to_arabic('MMMCMXCIX'), 3999)
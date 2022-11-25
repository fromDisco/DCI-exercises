import unittest
from string_operations import titlelize, unite_names


class Test_Strings(unittest.TestCase):

    def test_titelize(self):
        self.assertEqual(titlelize("name1", "name2"), ("Name1", "Name2"))

    def test_unite_names(self):
        self.assertEqual(unite_names(["Name1", "Name2"]), "Name1 Name2")
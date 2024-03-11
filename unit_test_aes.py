# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:24:06 2024

@author: JoelT
"""
import unittest
from aes import BinaryPolynomial


class TestBinaryPolynomial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.examples = [BinaryPolynomial(i) for i in range(4)]
        cls.correct_coefficients = [0, 1, 2, 3]
        cls.correct_less_significant_bit = [None, 0, 1, 0]
        cls.correct_most_significant_bit = [None, 0, 1, 1]

    def test_value_coefficients(self):
        """
        Evaluates if the setter and getter "coefficients" of the class works
        properlly.

        Returns
        -------
        None.

        """
        for i in range(len(self.correct_coefficients)):
            with self.subTest(number=self.correct_coefficients[i]):
                self.assertEqual(
                    self.correct_coefficients[i], self.examples[i].coefficients
                )

    def test_value_less_significant_bit(self):
        """
        Evaluates if the getter "less_significant_bit" of the class works
        properlly.
        Returns
        -------
        None.

        """

        for i in range(len(self.correct_coefficients)):
            with self.subTest(number=self.correct_coefficients[i]):
                self.assertEqual(
                    self.correct_less_significant_bit[i],
                    self.examples[i].less_significant_bit,
                )

    def test_value_most_significant_bit(self):
        """
        Evaluates if the getter "most_significant_bit" of the class works
        properlly.
        Returns
        -------
        None.

        """

        for i in range(len(self.correct_coefficients)):
            with self.subTest(number=self.correct_coefficients[i]):
                self.assertEqual(
                    self.correct_most_significant_bit[i],
                    self.examples[i].most_significant_bit,
                )


if __name__ == "__main__":
    unittest.main()

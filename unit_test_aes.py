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
        cls.correct_addition = [
            BinaryPolynomial(0),
            BinaryPolynomial(1),
            BinaryPolynomial(2),
            BinaryPolynomial(3),
            BinaryPolynomial(57),
            BinaryPolynomial(83),
            BinaryPolynomial(1),
            BinaryPolynomial(0),
            BinaryPolynomial(3),
            BinaryPolynomial(2),
            BinaryPolynomial(56),
            BinaryPolynomial(82),
            BinaryPolynomial(2),
            BinaryPolynomial(3),
            BinaryPolynomial(0),
            BinaryPolynomial(1),
            BinaryPolynomial(55),
            BinaryPolynomial(81),
            BinaryPolynomial(3),
            BinaryPolynomial(2),
            BinaryPolynomial(1),
            BinaryPolynomial(0),
            BinaryPolynomial(54),
            BinaryPolynomial(80),
            BinaryPolynomial(57),
            BinaryPolynomial(56),
            BinaryPolynomial(55),
            BinaryPolynomial(0),
            BinaryPolynomial(324),
            BinaryPolynomial(83),
            BinaryPolynomial(82),
            BinaryPolynomial(81),
            BinaryPolynomial(80),
            BinaryPolynomial(324),
            BinaryPolynomial(0),
        ]
        cls.examples = [
            BinaryPolynomial(0),
            BinaryPolynomial(1),
            BinaryPolynomial(2),
            BinaryPolynomial(3),
            BinaryPolynomial(57),
            BinaryPolynomial(83),
        ]
        cls.correct_coefficients = [0, 1, 2, 3]
        cls.correct_less_significant_bit = [None, 0, 1, 0]
        cls.correct_most_significant_bit = [None, 0, 1, 1]
        cls.correct_substraction = [
            BinaryPolynomial(0),
            BinaryPolynomial(1),
            BinaryPolynomial(2),
            BinaryPolynomial(3),
            BinaryPolynomial(57),
            BinaryPolynomial(83),
            BinaryPolynomial(1),
            BinaryPolynomial(0),
            BinaryPolynomial(3),
            BinaryPolynomial(2),
            BinaryPolynomial(56),
            BinaryPolynomial(82),
            BinaryPolynomial(2),
            BinaryPolynomial(3),
            BinaryPolynomial(0),
            BinaryPolynomial(1),
            BinaryPolynomial(55),
            BinaryPolynomial(81),
            BinaryPolynomial(3),
            BinaryPolynomial(2),
            BinaryPolynomial(1),
            BinaryPolynomial(0),
            BinaryPolynomial(54),
            BinaryPolynomial(80),
            BinaryPolynomial(57),
            BinaryPolynomial(56),
            BinaryPolynomial(55),
            BinaryPolynomial(0),
            BinaryPolynomial(324),
            BinaryPolynomial(83),
            BinaryPolynomial(82),
            BinaryPolynomial(81),
            BinaryPolynomial(80),
            BinaryPolynomial(324),
            BinaryPolynomial(0),
        ]

    def test_add(self):
        """
        Evaluates if the method of addition operates properly.

        Returns
        -------
        None.

        """
        for i in range(len(self.correct_coefficients)):
            for j in range(len(self.correct_coefficients)):
                with self.subTest(
                    a=self.correct_coefficients[i],
                    b=self.correct_coefficients[j],
                    i=4 * i + j,
                ):
                    self.assertEqual(
                        self.correct_addition[4 * i + j],
                        self.examples[i] + self.examples[j],
                    )

    def test_sub(self):
        """
        Evaluates if the method of substraction operates properly.

        Returns
        -------
        None.

        """
        for i in range(len(self.correct_coefficients)):
            for j in range(len(self.correct_coefficients)):
                with self.subTest(
                    a=self.correct_coefficients[i],
                    b=self.correct_coefficients[j],
                    i=4 * i + j,
                ):
                    self.assertEqual(
                        self.correct_substraction[4 * i + j],
                        self.examples[i] - self.examples[j],
                    )

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

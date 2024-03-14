# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:46:43 2024

@author: JoelT
"""
import unittest
from binary_polynomial import BinaryPolynomial


class TestBinaryPolynomial(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.correct_addition = [
            BinaryPolynomial(0),  # 0000 0000 + 0000 0000 = 0000 0000
            BinaryPolynomial(1),  # 0000 0000 + 0000 0001 = 0000 0001
            BinaryPolynomial(2),  # 0000 0000 + 0000 0010 = 0000 0010
            BinaryPolynomial(3),  # 0000 0000 + 0000 0011 = 0000 0011
            BinaryPolynomial(87),  # 0000 0000 + 0101 0111 = 0101 0111
            BinaryPolynomial(131),  # 0000 0000 + 1000 0011 = 1000 0011
            BinaryPolynomial(1),  # 0000 0001 + 0000 0000 = 0000 0001
            BinaryPolynomial(0),  # 0000 0001 + 0000 0001 = 0000 0000
            BinaryPolynomial(3),  # 0000 0001 + 0000 0010 = 0000 0011
            BinaryPolynomial(2),  # 0000 0001 + 0000 0011 = 0000 0010
            BinaryPolynomial(86),  # 0000 0001 + 0101 0111 = 0101 0110
            BinaryPolynomial(130),  # 0000 0001 + 1000 0011 = 1000 0010
            BinaryPolynomial(2),  # 0000 0010 + 0000 0000 = 0000 0010
            BinaryPolynomial(3),  # 0000 0010 + 0000 0001 = 0000 0011
            BinaryPolynomial(0),  # 0000 0010 + 0000 0010 = 0000 0000
            BinaryPolynomial(1),  # 0000 0010 + 0000 0011 = 0000 0001
            BinaryPolynomial(85),  # 0000 0010 + 0101 0111 = 0101 0101
            BinaryPolynomial(129),  # 0000 0010 + 1000 0011 = 1000 0001
            BinaryPolynomial(3),  # 0000 0011 + 0000 0000 = 0000 0011
            BinaryPolynomial(2),  # 0000 0011 + 0000 0001 = 0000 0010
            BinaryPolynomial(1),  # 0000 0011 + 0000 0010 = 0000 0001
            BinaryPolynomial(0),  # 0000 0011 + 0000 0011 = 0000 0000
            BinaryPolynomial(84),  # 0000 0011 + 0101 0111 = 0101 0100
            BinaryPolynomial(128),  # 0000 0011 + 1000 0011 = 1000 0000
            BinaryPolynomial(87),  # 0101 0111 + 0000 0000 = 0101 0111
            BinaryPolynomial(86),  # 0101 0111 + 0000 0001 = 0101 0110
            BinaryPolynomial(85),  # 0101 0111 + 0000 0010 = 0101 0101
            BinaryPolynomial(84),  # 0101 0111 + 0000 0011 = 0101 0100
            BinaryPolynomial(0),  # 0101 0111 + 0101 0111 = 0000 0000
            BinaryPolynomial(212),  # 0101 0111 + 1000 0011 = 1101 0100
            BinaryPolynomial(131),  # 1000 0011 + 0000 0000 = 1000 0011
            BinaryPolynomial(130),  # 1000 0011 + 0000 0001 = 1000 0010
            BinaryPolynomial(129),  # 1000 0011 + 0000 0010 = 1000 0001
            BinaryPolynomial(128),  # 1000 0011 + 0000 0011 = 1000 000
            BinaryPolynomial(212),  # 1000 0011 + 0101 0111 = 1101 0100
            BinaryPolynomial(0),  # 1000 0011 + 1000 0011 = 0000 0000
        ]
        cls.correct_coefficients = [
            0,  # 0000 0000
            1,  # 0000 0001
            2,  # 0000 0010
            3,  # 0000 0011
            87,  # 0101 0111
            131,  # 1000 0011
        ]
        cls.correct_greater = [
            cls.assertFalse,  # 0000 0000 > 0000 0000 = False
            cls.assertFalse,  # 0000 0000 > 0000 0001 = False
            cls.assertFalse,  # 0000 0000 > 0000 0010 = False
            cls.assertFalse,  # 0000 0000 > 0000 0011 = False
            cls.assertFalse,  # 0000 0000 > 0101 0111 = False
            cls.assertFalse,  # 0000 0000 > 1000 0011 = False
            cls.assertTrue,  # 0000 0001 > 0000 0000 = True
            cls.assertFalse,  # 0000 0001 > 0000 0001 = False
            cls.assertFalse,  # 0000 0001 > 0000 0010 = False
            cls.assertFalse,  # 0000 0001 > 0000 0011 = False
            cls.assertFalse,  # 0000 0001 > 0101 0111 = False
            cls.assertFalse,  # 0000 0001 > 1000 0011 = False
            cls.assertTrue,  # 0000 0010 > 0000 0000 = True
            cls.assertTrue,  # 0000 0010 > 0000 0001 = True
            cls.assertFalse,  # 0000 0010 > 0000 0010 = False
            cls.assertFalse,  # 0000 0010 > 0000 0011 = False
            cls.assertFalse,  # 0000 0010 > 0101 0111 = False
            cls.assertFalse,  # 0000 0010 > 1000 0011 = False
            cls.assertTrue,  # 0000 0011 > 0000 0000 = True
            cls.assertTrue,  # 0000 0011 > 0000 0001 = True
            cls.assertTrue,  # 0000 0011 > 0000 0010 = True
            cls.assertFalse,  # 0000 0011 > 0000 0011 = False
            cls.assertFalse,  # 0000 0011 > 0101 0111 = False
            cls.assertFalse,  # 0000 0011 > 1000 0011 = False
            cls.assertTrue,  # 0101 0111 > 0000 0000 = True
            cls.assertTrue,  # 0101 0111 > 0000 0001 = True
            cls.assertTrue,  # 0101 0111 > 0000 0010 = True
            cls.assertTrue,  # 0101 0111 > 0000 0011 = True
            cls.assertFalse,  # 0101 0111 > 0101 0111 = False
            cls.assertFalse,  # 0101 0111 > 1000 0011 = False
            cls.assertTrue,  # 1000 0011 > 0000 0000 = True
            cls.assertTrue,  # 1000 0011 > 0000 0001 = True
            cls.assertTrue,  # 1000 0011 > 0000 0010 = True
            cls.assertTrue,  # 1000 0011 > 0000 0011 = True
            cls.assertTrue,  # 1000 0011 > 0101 0111 = True
            cls.assertFalse,  # 1000 0011 > 1000 0011 = False
        ]
        cls.correct_greater_or_equal = [
            cls.assertTrue,  # 0000 0000 => 0000 0000 = True
            cls.assertFalse,  # 0000 0000 => 0000 0001 = False
            cls.assertFalse,  # 0000 0000 => 0000 0010 = False
            cls.assertFalse,  # 0000 0000 => 0000 0011 = False
            cls.assertFalse,  # 0000 0000 => 0101 0111 = False
            cls.assertFalse,  # 0000 0000 => 1000 0011 = False
            cls.assertTrue,  # 0000 0001 => 0000 0000 = True
            cls.assertTrue,  # 0000 0001 => 0000 0001 = True
            cls.assertFalse,  # 0000 0001 => 0000 0010 = False
            cls.assertFalse,  # 0000 0001 => 0000 0011 = False
            cls.assertFalse,  # 0000 0001 => 0101 0111 = False
            cls.assertFalse,  # 0000 0001 => 1000 0011 = False
            cls.assertTrue,  # 0000 0010 => 0000 0000 = True
            cls.assertTrue,  # 0000 0010 => 0000 0001 = True
            cls.assertTrue,  # 0000 0010 => 0000 0010 = True
            cls.assertFalse,  # 0000 0010 => 0000 0011 = False
            cls.assertFalse,  # 0000 0010 => 0101 0111 = False
            cls.assertFalse,  # 0000 0010 => 1000 0011 = False
            cls.assertTrue,  # 0000 0011 => 0000 0000 = True
            cls.assertTrue,  # 0000 0011 => 0000 0001 = True
            cls.assertTrue,  # 0000 0011 => 0000 0010 = True
            cls.assertTrue,  # 0000 0011 => 0000 0011 = True
            cls.assertFalse,  # 0000 0011 => 0101 0111 = False
            cls.assertFalse,  # 0000 0011 => 1000 0011 = False
            cls.assertTrue,  # 0101 0111 => 0000 0000 = True
            cls.assertTrue,  # 0101 0111 => 0000 0001 = True
            cls.assertTrue,  # 0101 0111 => 0000 0010 = True
            cls.assertTrue,  # 0101 0111 => 0000 0011 = True
            cls.assertTrue,  # 0101 0111 => 0101 0111 = True
            cls.assertFalse,  # 0101 0111 => 1000 0011 = False
            cls.assertTrue,  # 1000 0011 => 0000 0000 = True
            cls.assertTrue,  # 1000 0011 => 0000 0001 = True
            cls.assertTrue,  # 1000 0011 => 0000 0010 = True
            cls.assertTrue,  # 1000 0011 => 0000 0011 = True
            cls.assertTrue,  # 1000 0011 => 0101 0111 = True
            cls.assertTrue,  # 1000 0011 => 1000 0011 = True
        ]
        cls.correct_less_significant_bit = [
            None,  # None
            0,  # 0000 0001
            1,  # 0000 0010
            0,  # 0000 0001
            0,  # 0000 0001
            0,  # 0000 0001
        ]
        cls.correct_less_or_equal = [
            cls.assertTrue,  # 0000 0000 <= 0000 0000 = True
            cls.assertTrue,  # 0000 0000 <= 0000 0001 = True
            cls.assertTrue,  # 0000 0000 <= 0000 0010 = True
            cls.assertTrue,  # 0000 0000 <= 0000 0011 = True
            cls.assertTrue,  # 0000 0000 <= 0101 0111 = True
            cls.assertTrue,  # 0000 0000 <= 1000 0011 = True
            cls.assertFalse,  # 0000 0001 <= 0000 0000 = False
            cls.assertTrue,  # 0000 0001 <= 0000 0001 = True
            cls.assertTrue,  # 0000 0001 <= 0000 0010 = True
            cls.assertTrue,  # 0000 0001 <= 0000 0011 = True
            cls.assertTrue,  # 0000 0001 <= 0101 0111 = True
            cls.assertTrue,  # 0000 0001 <= 1000 0011 = True
            cls.assertFalse,  # 0000 0010 <= 0000 0000 = False
            cls.assertFalse,  # 0000 0010 <= 0000 0001 = False
            cls.assertTrue,  # 0000 0010 <= 0000 0010 = True
            cls.assertTrue,  # 0000 0010 <= 0000 0011 = True
            cls.assertTrue,  # 0000 0010 <= 0101 0111 = True
            cls.assertTrue,  # 0000 0010 <= 1000 0011 = True
            cls.assertFalse,  # 0000 0011 <= 0000 0000 = False
            cls.assertFalse,  # 0000 0011 <= 0000 0001 = False
            cls.assertFalse,  # 0000 0011 <= 0000 0010 = False
            cls.assertTrue,  # 0000 0011 <= 0000 0011 = True
            cls.assertTrue,  # 0000 0011 <= 0101 0111 = True
            cls.assertTrue,  # 0000 0011 <= 1000 0011 = True
            cls.assertFalse,  # 0101 0111 <= 0000 0000 = False
            cls.assertFalse,  # 0101 0111 <= 0000 0001 = False
            cls.assertFalse,  # 0101 0111 <= 0000 0010 = False
            cls.assertFalse,  # 0101 0111 <= 0000 0011 = False
            cls.assertTrue,  # 0101 0111 <= 0101 0111 = True
            cls.assertTrue,  # 0101 0111 <= 1000 0011 = True
            cls.assertFalse,  # 1000 0011 <= 0000 0000 = False
            cls.assertFalse,  # 1000 0011 <= 0000 0001 = False
            cls.assertFalse,  # 1000 0011 <= 0000 0010 = False
            cls.assertFalse,  # 1000 0011 <= 0000 0011 = False
            cls.assertFalse,  # 1000 0011 <= 0101 0111 = False
            cls.assertTrue,  # 1000 0011 <= 1000 0011 = True
        ]
        cls.correct_lesser = [
            cls.assertFalse,  # 0000 0000 < 0000 0000 = False
            cls.assertTrue,  # 0000 0000 < 0000 0001 = True
            cls.assertTrue,  # 0000 0000 < 0000 0010 = True
            cls.assertTrue,  # 0000 0000 < 0000 0011 = True
            cls.assertTrue,  # 0000 0000 < 0101 0111 = True
            cls.assertTrue,  # 0000 0000 < 1000 0011 = True
            cls.assertFalse,  # 0000 0001 < 0000 0000 = False
            cls.assertFalse,  # 0000 0001 < 0000 0001 = False
            cls.assertTrue,  # 0000 0001 < 0000 0010 = True
            cls.assertTrue,  # 0000 0001 < 0000 0011 = True
            cls.assertTrue,  # 0000 0001 < 0101 0111 = True
            cls.assertTrue,  # 0000 0001 < 1000 0011 = True
            cls.assertFalse,  # 0000 0010 < 0000 0000 = False
            cls.assertFalse,  # 0000 0010 < 0000 0001 = False
            cls.assertFalse,  # 0000 0010 < 0000 0010 = False
            cls.assertTrue,  # 0000 0010 < 0000 0011 = True
            cls.assertTrue,  # 0000 0010 < 0101 0111 = True
            cls.assertTrue,  # 0000 0010 < 1000 0011 = True
            cls.assertFalse,  # 0000 0011 < 0000 0000 = False
            cls.assertFalse,  # 0000 0011 < 0000 0001 = False
            cls.assertFalse,  # 0000 0011 < 0000 0010 = False
            cls.assertFalse,  # 0000 0011 < 0000 0011 = False
            cls.assertTrue,  # 0000 0011 < 0101 0111 = True
            cls.assertTrue,  # 0000 0011 < 1000 0011 = True
            cls.assertFalse,  # 0101 0111 < 0000 0000 = False
            cls.assertFalse,  # 0101 0111 < 0000 0001 = False
            cls.assertFalse,  # 0101 0111 < 0000 0010 = False
            cls.assertFalse,  # 0101 0111 < 0000 0011 = False
            cls.assertFalse,  # 0101 0111 < 0101 0111 = False
            cls.assertTrue,  # 0101 0111 < 1000 0011 = True
            cls.assertFalse,  # 1000 0011 < 0000 0000 = False
            cls.assertFalse,  # 1000 0011 < 0000 0001 = False
            cls.assertFalse,  # 1000 0011 < 0000 0010 = False
            cls.assertFalse,  # 1000 0011 < 0000 0011 = False
            cls.assertFalse,  # 1000 0011 < 0101 0111 = False
            cls.assertFalse,  # 1000 0011 < 1000 0011 = False
        ]
        cls.correct_most_significant_bit = [
            None,  # None
            0,  # 0000 0000
            1,  # 0000 0001
            1,  # 0000 0001
            6,  # 0100 0000
            7,  # 1000 0000
        ]
        cls.correct_substraction = [
            BinaryPolynomial(0),  # 0000 0000 - 0000 0000 = 0000 0000
            BinaryPolynomial(1),  # 0000 0000 - 0000 0001 = 0000 0001
            BinaryPolynomial(2),  # 0000 0000 - 0000 0010 = 0000 0010
            BinaryPolynomial(3),  # 0000 0000 - 0000 0011 = 0000 0011
            BinaryPolynomial(87),  # 0000 0000 - 0101 0111 = 0101 0111
            BinaryPolynomial(131),  # 0000 0000 - 1000 0011 = 1000 0011
            BinaryPolynomial(1),  # 0000 0001 - 0000 0000 = 0000 0001
            BinaryPolynomial(0),  # 0000 0001 - 0000 0001 = 0000 0000
            BinaryPolynomial(3),  # 0000 0001 - 0000 0010 = 0000 0011
            BinaryPolynomial(2),  # 0000 0001 - 0000 0011 = 0000 0010
            BinaryPolynomial(86),  # 0000 0001 - 0101 0111 = 0101 0110
            BinaryPolynomial(130),  # 0000 0001 - 1000 0011 = 1000 0010
            BinaryPolynomial(2),  # 0000 0010 - 0000 0000 = 0000 0010
            BinaryPolynomial(3),  # 0000 0010 - 0000 0001 = 0000 0011
            BinaryPolynomial(0),  # 0000 0010 - 0000 0010 = 0000 0000
            BinaryPolynomial(1),  # 0000 0010 - 0000 0011 = 0000 0001
            BinaryPolynomial(85),  # 0000 0010 - 0101 0111 = 0101 0101
            BinaryPolynomial(129),  # 0000 0010 - 1000 0011 = 1000 0001
            BinaryPolynomial(3),  # 0000 0011 - 0000 0000 = 0000 0011
            BinaryPolynomial(2),  # 0000 0011 - 0000 0001 = 0000 0010
            BinaryPolynomial(1),  # 0000 0011 - 0000 0010 = 0000 0001
            BinaryPolynomial(0),  # 0000 0011 - 0000 0011 = 0000 0000
            BinaryPolynomial(84),  # 0000 0011 - 0101 0111 = 0101 0100
            BinaryPolynomial(128),  # 0000 0011 - 1000 0011 = 1000 0000
            BinaryPolynomial(87),  # 0101 0111 - 0000 0000 = 0101 0111
            BinaryPolynomial(86),  # 0101 0111 - 0000 0001 = 0101 0110
            BinaryPolynomial(85),  # 0101 0111 - 0000 0010 = 0101 0101
            BinaryPolynomial(84),  # 0101 0111 - 0000 0011 = 0101 0100
            BinaryPolynomial(0),  # 0101 0111 - 0101 0111 = 0000 0000
            BinaryPolynomial(212),  # 0101 0111 - 1000 0011 = 1101 0100
            BinaryPolynomial(131),  # 1000 0011 - 0000 0000 = 1000 0011
            BinaryPolynomial(130),  # 1000 0011 - 0000 0001 = 1000 0010
            BinaryPolynomial(129),  # 1000 0011 - 0000 0010 = 1000 0001
            BinaryPolynomial(128),  # 1000 0011 - 0000 0011 = 1000 000
            BinaryPolynomial(212),  # 1000 0011 - 0101 0111 = 1101 0100
            BinaryPolynomial(0),  # 1000 0011 - 1000 0011 = 0000 0000
        ]
        cls.examples = [
            BinaryPolynomial(0),  # 0000 0000
            BinaryPolynomial(1),  # 0000 0001
            BinaryPolynomial(2),  # 0000 0010
            BinaryPolynomial(3),  # 0000 0011
            BinaryPolynomial(87),  # 0101 0111
            BinaryPolynomial(131),  # 1000 0011
        ]

        cls.N = len(cls.examples)

    def test_add(self):
        """
        Evaluates if the method of addition operates properly.

        Returns
        -------
        None.

        """
        for i in range(self.N):
            for j in range(self.N):
                with self.subTest(
                    a=self.correct_coefficients[i],
                    b=self.correct_coefficients[j],
                    i=self.N * i + j,
                ):
                    self.assertEqual(
                        self.correct_addition[self.N * i + j],
                        self.examples[i] + self.examples[j],
                    )

    def test_eq(self):
        """
        Evaluates if the equal method works properly.

        Returns
        -------
        None.

        """
        for i, j in zip(self.examples, self.examples):
            with self.subTest(a=i, b=j):
                self.assertTrue(i == j)

        for i, j in zip(self.examples, self.examples[::-1]):
            with self.subTest(a=i, b=j):
                self.assertFalse(i == j)

    def test_ge(self):
        """
        Evaluates if the greater-or-equal-than method works properly.

        Returns
        -------
        None.

        """
        for i in range(self.N):
            for j in range(self.N):
                with self.subTest(
                    a=self.correct_coefficients[i],
                    b=self.correct_coefficients[j],
                    i=self.N * i + j,
                ):
                    self.correct_greater_or_equal[self.N * i + j](
                        self, self.examples[i] >= self.examples[j]
                    )

    def test_gt(self):
        """
        Evaluates if the greater-than method works properly.

        Returns
        -------
        None.

        """
        for i in range(self.N):
            for j in range(self.N):
                with self.subTest(
                    a=self.correct_coefficients[i],
                    b=self.correct_coefficients[j],
                    i=self.N * i + j,
                ):
                    self.correct_greater[self.N * i + j](
                        self, self.examples[i] > self.examples[j]
                    )

    def test_le(self):
        """
        Evaluates if the less-or-equal-than method works properly.

        Returns
        -------
        None.

        """
        for i in range(self.N):
            for j in range(self.N):
                with self.subTest(
                    a=self.correct_coefficients[i],
                    b=self.correct_coefficients[j],
                    i=self.N * i + j,
                ):
                    self.correct_less_or_equal[self.N * i + j](
                        self, self.examples[i] <= self.examples[j]
                    )

    def test_lt(self):
        """
        Evaluates if the less-than method works properly.

        Returns
        -------
        None.

        """
        for i in range(self.N):
            for j in range(self.N):
                with self.subTest(
                    a=self.correct_coefficients[i],
                    b=self.correct_coefficients[j],
                    i=self.N * i + j,
                ):
                    self.correct_lesser[self.N * i + j](
                        self, self.examples[i] < self.examples[j]
                    )

    def test_ne(self):
        """
        Evaluates if the not equal method works properly.

        Returns
        -------
        None.

        """
        for i, j in zip(self.examples, self.examples):
            with self.subTest(a=i, b=j):
                self.assertFalse(i != j)

        for i, j in zip(self.examples, self.examples[::-1]):
            with self.subTest(a=i, b=j):
                self.assertTrue(i != j)

    def test_sub(self):
        """
        Evaluates if the method of substraction operates properly.

        Returns
        -------
        None.

        """
        for i in range(self.N):
            for j in range(self.N):
                with self.subTest(
                    a=self.correct_coefficients[i],
                    b=self.correct_coefficients[j],
                    i=len(self.examples) * i + j,
                ):
                    self.assertEqual(
                        self.correct_substraction[self.N * i + j],
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
        for correct, test in zip(self.correct_coefficients, self.examples):
            with self.subTest(number=correct):
                self.assertEqual(correct, test.coefficients)

    def test_value_less_significant_bit(self):
        """
        Evaluates if the getter "less_significant_bit" of the class works
        properlly.
        Returns
        -------
        None.

        """

        for correct, test in zip(
            self.correct_less_significant_bit, self.examples
        ):
            with self.subTest(number=correct):
                self.assertEqual(correct, test.less_significant_bit)

    def test_value_most_significant_bit(self):
        """
        Evaluates if the getter "most_significant_bit" of the class works
        properlly.
        Returns
        -------
        None.

        """

        for correct, test in zip(
            self.correct_most_significant_bit, self.examples
        ):
            with self.subTest(number=correct):
                self.assertEqual(correct, test.most_significant_bit)

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
        cls.examples = [
            BinaryPolynomial(0),  # 0000 0000
            BinaryPolynomial(1),  # 0000 0001
            BinaryPolynomial(2),  # 0000 0010
            BinaryPolynomial(3),  # 0000 0011
            BinaryPolynomial(87),  # 0101 0111
            BinaryPolynomial(131),  # 1000 0011
        ]
        cls.correct_coefficients = [
            0,  # 0000 0000
            1,  # 0000 0001
            2,  # 0000 0010
            3,  # 0000 0011
            87,  # 0101 0111
            131,  # 1000 0011
        ]
        cls.correct_less_significant_bit = [
            None,  # None
            0,  # 0000 0001
            1,  # 0000 0010
            0,  # 0000 0001
            0,  # 0000 0001
            0,  # 0000 0001
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

        cls.__N = len(cls.examples)

    def test_add(self):
        """
        Evaluates if the method of addition operates properly.

        Returns
        -------
        None.

        """
        for i in range(self.__N):
            for j in range(self.__N):
                with self.subTest(
                    a=self.correct_coefficients[i],
                    b=self.correct_coefficients[j],
                    i=len(self.examples) * i + j,
                ):
                    self.assertEqual(
                        self.correct_addition[self.__N * i + j],
                        self.examples[i] + self.examples[j],
                    )

    def test_sub(self):
        """
        Evaluates if the method of substraction operates properly.

        Returns
        -------
        None.

        """
        for i in range(self.__N):
            for j in range(self.__N):
                with self.subTest(
                    a=self.correct_coefficients[i],
                    b=self.correct_coefficients[j],
                    i=len(self.examples) * i + j,
                ):
                    self.assertEqual(
                        self.correct_substraction[self.__N * i + j],
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
        for i in range(self.__N):
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

        for i in range(self.__N):
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

        for i in range(self.__N):
            with self.subTest(number=self.correct_coefficients[i]):
                self.assertEqual(
                    self.correct_most_significant_bit[i],
                    self.examples[i].most_significant_bit,
                )


if __name__ == "__main__":
    unittest.main()

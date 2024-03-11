# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:03:04 2024

@author: JoelT
"""
from math import log


class BinaryPolynomial:
    __slots__ = (
        "__coefficients",
        "__most_significant_bit",
        "__less_significant_bit",
    )

    def __init__(self, number: int):
        self.__coefficients = number
        self.__most_significant_bit = (
            self.__calculate_most_significant_bit_number()
        )
        self.__less_significant_bit = (
            self.__calculate_less_significant_bit_number()
        )

    def __calculate_most_significant_bit_number(self) -> int:
        """
        When the quoeficients value are set this calculate at 0(1) time the
        Most Significant Bit (MSB).

        Returns
        -------
        int
            Position of the Most Significant Bit (MSB).

        """
        # Below steps set bits after
        # MSB (including MSB)

        bit_array = self.__coefficients

        # Suppose bit_array is 273 (binary
        # is 100010001). It does following
        # 100010001 | 010001000 = 110011001
        bit_array |= bit_array >> 1

        # This makes sure 4 bits
        # (From MSB and including MSB)
        # are set. It does following
        # 110011001 | 001100110 = 111111111
        bit_array |= bit_array >> 2

        bit_array |= bit_array >> 4
        bit_array |= bit_array >> 8
        bit_array |= bit_array >> 16

        # Increment bit_array by 1 so that
        # there is only one set bit
        # which is just before original
        # MSB. bit_array now becomes 1000000000
        bit_array = bit_array + 1

        # Set MSB after shifting.
        # bit_array now becomes 100000000
        bit_array >>= 1

        if bit_array == 0:
            return None

        return int(log(bit_array, 2))

    def __calculate_less_significant_bit_number(self) -> int:
        """
        When the quoeficients value are set this calculate at 0(1) time the
        Less Significant Bit (LSB).

        Returns
        -------
        int
            Position of the Less Significant Bit (LSB).

        """
        bit_array = self.__coefficients

        bit_array &= -bit_array

        if bit_array == 0:
            return None

        return int(log(bit_array, 2))

    @property
    def most_significant_bit(self) -> int:
        """
        PGetter of the property that has stored the position of the Most
        Significant Bit (MSB).

        Returns
        -------
        int
            Position of the Most Significant Bit (MSB).

        """
        return self.__most_significant_bit

    @property
    def less_significant_bit(self) -> int:
        """
        Getter of the property that has stored the position of the Less
        Significant Bit (LSB).

        Returns
        -------
        int
            Position of the Less Significant Bit (LSB).

        """
        return self.__less_significant_bit

    @property
    def coefficients(self) -> int:
        """
        Getter of the property that has stored the quoeficients bit arrays.

        Returns
        -------
        int
            Bit array of the quoeficients of the polynomial.

        """
        return self.__coefficients

    @coefficients.setter
    def coefficients(self, number: int):
        if not isinstance(number, int):
            raise ValueError(
                "Number must be an integer value representing a bit array"
            )

        if number < 0:
            raise ValueError(
                "Number must be positive to represent a bit array of "
                + "polinomial quoficients."
            )

        self.__coefficients = number
        self.__most_significant_bit = (
            self.__calculate_most_significant_bit_number()
        )
        self.__less_significant_bit = (
            self.__calculate_less_significant_bit_number()
        )

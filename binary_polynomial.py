# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:45:23 2024

@author: JoelT
"""
from math import log
from typing import List


class BinaryPolynomial:
    __slots__ = (
        "__coefficients",
        "__less_significant_bit",
        "__most_significant_bit",
        "__supertext_map",
    )

    def __init__(self, number: int):
        self.__coefficients: int = number
        self.__less_significant_bit: int | None = (
            self.__calculate_less_significant_bit_number()
        )
        self.__most_significant_bit: int | None = (
            self.__calculate_most_significant_bit_number()
        )

        self.__supertext_map = {
            "0": "\u2070",
            "1": "\u00B9",
            "2": "\u00B2",
            "3": "\u00B3",
            "4": "\u2074",
            "5": "\u2075",
            "6": "\u2076",
            "7": "\u2077",
            "8": "\u2078",
            "9": "\u2079",
        }

    def __add__(self, binary_polynomial):
        """
        Calculates the addition of both polynomial in the
        (Z_2[x]/m(x),⊕,⊗) with m(x) = x^8 + x^4 + x^3 + x + 1.

        Parameters
        ----------
        binary_polynomial : BinaryPolynomial
            BinaryPolynomial class object.

        Returns
        -------
        BinaryPolynomial
            Returns a BinaryPolynomial object with the coefficients as the
            result of the addition.

        """
        return BinaryPolynomial(
            self.coefficients ^ binary_polynomial.coefficients
        )

    def __calculate_less_significant_bit_number(self) -> int | None:
        """
        When the quoeficients value are set this calculate at 0(1) time the
        Less Significant Bit (LSB).

        Returns
        -------
        Integer
            Position of the Less Significant Bit (LSB).
        None
            If there is no Significant Bit (all zeros).

        """
        bit_array: int = self.__coefficients

        bit_array &= -bit_array

        if bit_array == 0:
            return None

        return int(log(bit_array, 2))

    def __calculate_most_significant_bit_number(self) -> int | None:
        """
        When the quoeficients value are set this calculate at 0(1) time the
        Most Significant Bit (MSB).

        Returns
        -------
        Integer
            Position of the Most Significant Bit (MSB).
        None
            If there is no Significant Bit (all zeros).


        """
        # Below steps set bits after
        # MSB (including MSB)

        bit_array: int = self.__coefficients

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

    def __eq__(self, binary_polynomial) -> bool:
        """
        Compares the coefficients of two binary polynomials and returns if they
        are equal or not.

        Parameters
        ----------
        binary_polynomial : BinaryPolynomial
            BinaryPolynomial class object.

        Returns
        -------
        Boolean
            If the two binary polynomials are equal (True) or not (False).

        """
        return self.__coefficients == binary_polynomial.__coefficients

    def __ge__(self, binary_polynomial) -> bool:
        """
        Compares the coefficients of two binary polynomials and returns if the
        first polynomial is greater or equal than the second polynomial.

        Parameters
        ----------
        binary_polynomial : BinaryPolynomial
            BinaryPolynomial class object.

        Returns
        -------
        Boolean
            If the first polynomial is greater or equal (True) or not (False)
            than the second polynomial.

        """
        return (self > binary_polynomial) or (self == binary_polynomial)

    def __gt__(self, binary_polynomial) -> bool:
        """
        Compares the coefficients of two binary polynomials and returns if the
        first polynomial is greater than the second polynomial.

        Parameters
        ----------
        binary_polynomial : BinaryPolynomial
            BinaryPolynomial class object.

        Returns
        -------
        Boolean
            If the first polynomial is greater (True) or not (False) than the
            second polynomial.

        """
        return self.__coefficients > binary_polynomial.__coefficients

    def __index__(self) -> int:
        """
        Returns the decimal integer form of the coefficients.For the bin() and
        hex() functions.

        Returns
        -------
        Integer
            Decimal expresion of the binary coefficients.

        """
        return self.__coefficients

    def __mul__(self, binary_polynomial):
        """
        Calculates the multiplication of both polynomial in the
        (Z_2[x]/m(x),⊕,⊗) with m(x) = x^8 + x^4 + x^3 + x + 1.

        Parameters
        ----------
        binary_polynomial : BinaryPolynomial
            BinaryPolynomial class object.

        Returns
        -------
        BinaryPolynomial
            Returns a BinaryPolynomial object with the coefficients as the
            result of the addition.

        """
        # TODO
        pass

    def __ne__(self, binary_polynomial) -> bool:
        """
        Compares the coefficients of two binary polynomials and returns if they
        are not equal or not.

        Parameters
        ----------
        binary_polynomial : BinaryPolynomial
            BinaryPolynomial class object.

        Returns
        -------
        Boolean
            If the two binary polynomials are not equal (True) or not (False).

        """

        return not self == binary_polynomial

    def __le__(self, binary_polynomial) -> bool:
        """
        Compares the coefficients of two binary polynomials and returns if the
        first polynomial is lesser or equal than the second polynomial.

        Parameters
        ----------
        binary_polynomial : BinaryPolynomial
            BinaryPolynomial class object.

        Returns
        -------
        Boolean
            If the first polynomial is lesser or equal (True) or not (False)
            than the second polynomial.

        """
        return (self < binary_polynomial) or (self == binary_polynomial)

    def __lt__(self, binary_polynomial) -> bool:
        """
        Compares the coefficients of two binary polynomials and returns if the
        first polynomial is lesser than the second polynomial.

        Parameters
        ---------
        binary_polynomial : BinaryPolynomial
            BinaryPolynomial class object.

        Returns
        -------
        Boolean
            If the first polynomial is lesser (True) or not (False) than the
            second polynomial.

        """
        return self.__coefficients < binary_polynomial.__coefficients

    def __repr__(self) -> str:
        """
        Represents the debug information about the polynomia.

        Returns
        -------
        String
            String containing the debug information of the polynomial.

        """
        string: str = (
            "\nDEBUG INFORMATION\nPolynomial: "
            + str(self)
            + "\nCoefficients: "
            + str(self.__coefficients)
            + "\nLSB: "
            + str(self.__less_significant_bit)
            + "\nMSB: "
            + str(self.__most_significant_bit)
            + "\n"
        )
        return string

    def __str__(self) -> str:
        """
        Represent the polynomial as a string.

        Returns
        -------
        String
            String with the decimal expresion of the binary coefficients.

        """
        if self.__coefficients:
            binary_string: str = bin(self.coefficients)[2:]
            list_character: List[str] = [
                "1 * x" + self.__subscript(self.most_significant_bit - i)
                for i in range(self.most_significant_bit)
                if int(binary_string[i])
            ]

            string: str = " + ".join(list_character)

            if int(binary_string[-1]):
                if string != "":
                    string += " + "
                string += "1"

            return string
        return "0"

    def __sub__(self, binary_polynomial):
        """
        Calculates the substraction of both polynomial in the
        (Z_2[x]/m(x),⊕,⊗) with m(x) = x^8 + x^4 + x^3 + x + 1.

        Parameters
        ----------
        binary_polynomial : BinaryPolynomial
            BinaryPolynomial class object.

        Returns
        -------
        BinaryPolynomial
            Returns a BinaryPolynomial object with the coefficients as the
            result of the addition.

        """
        return BinaryPolynomial(
            self.coefficients ^ binary_polynomial.coefficients
        )

    def __subscript(self, number: int) -> str:
        string_number: str = str(number)
        string: str = ""
        for i in string_number:
            string += self.__supertext_map[i]
        return string

    @property
    def coefficients(self) -> int:
        """
        Getter of the property that has stored the quoeficients bit arrays.

        Returns
        -------
        Integer
            Bit array of the quoeficients of the polynomial.

        """
        return self.__coefficients

    @coefficients.setter
    def coefficients(self, number: int):
        """
        Setter of the property of the coefficients to a new value and
        recalculates the associated properties, updatign these too.

        Parameters
        ----------
        number : Integer
            Number equaling to the binary representation of the binary
            coefficients of the polynomial.

        Raises
        ------
        ValueError
            Data type of number is not a proper positive integer.

        Returns
        -------
        None.

        """
        if not isinstance(number, int):
            raise ValueError(
                "Number must be an integer value representing a bit array"
            )

        if number < 0:
            raise ValueError(
                "Number must be positive to represent a bit array of "
                + "polinomial quoficients."
            )

        self.__coefficients: int = number
        self.__most_significant_bit: int | None = (
            self.__calculate_most_significant_bit_number()
        )
        self.__less_significant_bit: int | None = (
            self.__calculate_less_significant_bit_number()
        )

    @property
    def less_significant_bit(self) -> int | None:
        """
        Getter of the property that has stored the position of the Less
        Significant Bit (LSB).

        Returns
        -------
        Integer
            Position of the Less Significant Bit (LSB).
        None
            If there is no Significant Bit (all zeros).

        """
        return self.__less_significant_bit

    @property
    def most_significant_bit(self) -> int | None:
        """
        Getter of the property that has stored the position of the Most
        Significant Bit (MSB).

        Returns
        -------
        Integer
            Position of the Most Significant Bit (MSB).
        None
            If there is no Significant Bit (all zeros).

        """
        return self.__most_significant_bit

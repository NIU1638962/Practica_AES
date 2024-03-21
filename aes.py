# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 13:03:04 2024

@author: JoelT
"""
from MixColumns import *
from ShiftRows import *
from SubBytes import *
from AES_constants import CAD

# En AES_constants.py o al inicio de tu script principal

def create_hex_matrix_from_string(input_string):
    # Asegura que la cadena tenga exactamente 16 caracteres
    padded_string = input_string.ljust(16)[:16]
    # Convierte la cadena a una matriz de estado 4x4
    return [[ord(c) for c in padded_string[i:i+4]] for i in range(0, 16, 4)]


def cifrar_aes(texto, clave):
    """
    Cifra el texto dado con la clave especificada usando AES-128.

    :param texto: Matriz 4x4 que representa el bloque de texto a cifrar.
    :param clave: Matriz 4x4 que representa la clave de cifrado AES-128.
    :return: Matriz 4x4 que representa el bloque de texto cifrado.
    """
    # Genera todas las claves de ronda a partir de la clave original
    round_keys = key_expansion(clave)
    
    # La primera operación AddRoundKey antes de las rondas de cifrado
    estado = add_round_key(texto, round_keys[0])
    
    # Aplica las rondas de cifrado
    for i in range(1, 10):  # AES-128 utiliza 10 rondas
        estado = sub_bytes(estado)
        estado = shift_rows(estado)
        estado = mix_columns(estado)
        estado = add_round_key(estado, round_keys[i])
    
    # Última ronda (sin MixColumns)
    estado = sub_bytes(estado)
    estado = shift_rows(estado)
    estado = add_round_key(estado, round_keys[-1])
    
    return estado

# Ejemplo de uso (esto es solo un ejemplo; en la práctica, necesitarías convertir texto y clave a formato de matriz)

clave = [[0x2b, 0x28, 0xab, 0x09], [0x7e, 0xae, 0xf7, 0xcf], [0x15, 0xd2, 0x15, 0x4f], [0x16, 0xa6, 0x88, 0x3c]]

texto_cifrado = cifrar_aes(create_hex_matrix_from_string(CAD), clave)

print("Texto cifrado:")
for row in texto_cifrado:
    print(' '.join(format(x, '02x') for x in row))

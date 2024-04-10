# AES.py
from AES_constants_and_tools import KEY, CAD_DEBUG, t
from Key_Expantion import key_expantion
from AddRoundKey import add_round_key
from ByteSub import sub_bytes
from ShiftRows import shift_rows
from MixColumns import mix_columns

def write_matrix_to_file(file, matrix, title="Matriz"):
    file.write(f"{title} = [\n")
    for row in matrix:
        row_str = ', '.join(f"0x{x:02x}" for x in row)
        file.write(f"    [{row_str}],\n")
    file.write("]\n\n")

def aes_encrypt(plaintext, key, filename="aes_output.txt"):
    state = plaintext
    with open(filename, 'w') as file:
        # Aplana la matriz 4x4 de la clave para la expansión
        key_flat = [byte for row in key for byte in row]
        expanded_key = key_expantion(key_flat)
        file.write("Expansión de la llave:\n")
        write_matrix_to_file(file, [expanded_key[i:i+16] for i in range(0, len(expanded_key), 16)], "Clave Expandida")

        # Genera las claves de ronda a partir de la clave expandida
        round_keys = []
        for r in range(11):
            round_key = expanded_key[16*r:16*(r+1)]
            round_key_matrix = [round_key[4*i:4*(i+1)] for i in range(4)]
            round_keys.append(round_key_matrix)
            
        write_matrix_to_file(file, state, "Input:")
        write_matrix_to_file(file, key, "Clave Inicial:")

        # Rondas de cifrado AES
        state = add_round_key(state, round_keys[0])  # Ronda inicial
        write_matrix_to_file(file, state, "Estado después de AddRoundKey 0")
        
        for i in range(1, 10):
            state = sub_bytes(state)
            write_matrix_to_file(file, state, f"Estado después de ByteSub {i}")
            state = shift_rows(state)
            write_matrix_to_file(file, state, f"Estado después de ShiftRows {i}")
            state = mix_columns(t(state))
            write_matrix_to_file(file, state, f"Estado después de MixColumns {i}")
            state = add_round_key(state, round_keys[i])
            write_matrix_to_file(file, state, f"Estado después de AddRoundKey {i}")
        
        # Última ronda (sin MixColumns)
        state = sub_bytes(state)
        write_matrix_to_file(file, state, f"Estado después de ByteSub {10}")
        state = shift_rows(state)
        write_matrix_to_file(file, state, f"Estado después de ShiftRows {10}")
        state = add_round_key(state, round_keys[10])
        write_matrix_to_file(file, state, f"Estado después de AddRoundKey {10}")

        write_matrix_to_file(file, state, "Output del cifrado:")

# Ejemplo de uso
if __name__ == "__main__":
    plaintext = CAD_DEBUG
    aes_encrypt(plaintext, KEY)
from AES_constants_and_tools import print_matrix, t


def shift_rows(state):
    """Aplica la operación ShiftRows al estado dado."""
    # Transpone la matriz para trabajar con las columnas
    transposed_state = t(state)
    new_state = [row[:] for row in transposed_state]  # Hacer una copia del estado para evitar mutación in-place
    for i in range(4):
        new_state[i] = transposed_state[i][i:] + transposed_state[i][:i]  # Desplaza las 'filas' que ahora son columnas
    # Transpone de nuevo para restaurar la estructura original
    return t(new_state)

if __name__ == "__main__":
    estado = [
        [0xd4, 0x27, 0x11, 0xae],
        [0xe0, 0xbf, 0x98, 0xf1],
        [0xb8, 0xb4, 0x5d, 0xe5],
        [0x1e, 0x41, 0x52, 0x30],
    ]

    print("Estado antes de ShiftRows:")
    print_matrix(estado)

    # Aplicar ShiftRows
    new_state = shift_rows(estado)

    print("\nEstado después de ShiftRows:")
    print_matrix(new_state)

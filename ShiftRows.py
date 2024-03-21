def shift_rows(state):
    """Aplica la operación ShiftRows al estado."""
    num_rows = 4  # AES siempre trabaja con una matriz de estado de 4x4

    for i in range(1, num_rows):  # Comenzar en 1 porque la primera fila no se rota
        state[i] = state[i][i:] + state[i][:i]

    return state

# Ejemplo de uso
state_after_sub_bytes = [
    [0x7a, 0xd5, 0x6b, 0x89],
    [0x2b, 0xc3, 0x9a, 0xf1],
    [0x30, 0x8c, 0xfd, 0x2f],
    [0x8d, 0x4e, 0x27, 0xbc]
]

# Aplica ShiftRows
new_state_after_shift_rows = shift_rows(state_after_sub_bytes)

# Imprime el estado después de aplicar ShiftRows
for row in new_state_after_shift_rows:
    print(' '.join(format(x, '02x') for x in row))

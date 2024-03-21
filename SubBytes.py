from AES_constants import S_BOX

def sub_bytes(state):
    """Aplica la transformación SubBytes en el estado usando la S-Box."""
    for i in range(len(state)):
        for j in range(len(state[i])):
            byte = state[i][j]
            # Accede directamente a la S-Box con el valor del byte
            state[i][j] = S_BOX[byte]
    return state


# Ejemplo de uso
state = [
    [0x32, 0x88, 0x31, 0xe0],
    [0x43, 0x5a, 0x31, 0x37],
    [0xf6, 0x30, 0x98, 0x07],
    [0xa8, 0x8d, 0xa2, 0x34]
]

# Aplica SubBytes
new_state = sub_bytes(state)

# Imprime el estado después de aplicar SubBytes
for row in new_state:
    print(' '.join(format(x, '02x') for x in row))

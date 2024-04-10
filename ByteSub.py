from AES_constants_and_tools import S_BOX, print_matrix

def sub_bytes(state):
    """Aplica la operación SubBytes usando la S_BOX."""
    for i in range(4):
        for j in range(4):
            byte = state[i][j]
            # Accede a S_BOX para la sustitución
            state[i][j] = S_BOX[byte]
    return state

if __name__ == "__main__":
    # Estado después de AddRoundKey (ejemplo, reemplaza con tu estado real)
    estado = [
    [0x19, 0xa0, 0x9a, 0xe9],
    [0x3d, 0xf4, 0xc6, 0xf8],
    [0xe3, 0xe2, 0x8d, 0x48],
    [0xbe, 0x2b, 0x2a, 0x08],
]
    print_matrix(estado, "Estado antes de ByteSub:")

    # Aplicar SubBytes
    new_state = sub_bytes(estado)

    # Imprimir el estado después de SubBytes
    print_matrix(new_state, "Estado después de ByteSub:")

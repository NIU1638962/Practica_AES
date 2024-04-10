# MixColumns.py
from AES_constants_and_tools import print_matrix, t

def xtime(a):
    """Realiza la multiplicación por x (es decir, {02}) en GF(2^8)."""
    return (((a << 1) & 0xFF) ^ (0x1B if (a & 0x80) else 0x00))

def mix_single_column(a):
    """Mezcla una sola columna."""
    # Ver la especificación de AES para detalles sobre esta operación
    t = a[0] ^ a[1] ^ a[2] ^ a[3]
    u = a[0]
    a[0] ^= t ^ xtime(a[0] ^ a[1])
    a[1] ^= t ^ xtime(a[1] ^ a[2])
    a[2] ^= t ^ xtime(a[2] ^ a[3])
    a[3] ^= t ^ xtime(a[3] ^ u)
    return a

def mix_columns(state):
    """Aplica MixColumns a todo el estado."""
    for i in range(4):
        column = [state[row][i] for row in range(4)]
        column = mix_single_column(column)
        for row in range(4):
            state[row][i] = column[row]
    return t(state)

if __name__ == "__main__":

    estado = [
    [0xd4, 0xbf, 0x5d, 0x30],
    [0xe0, 0xb4, 0x52, 0xae],
    [0xb8, 0x41, 0x11, 0xf1],
    [0x1e, 0x27, 0x98, 0xe5],
]
       
    print_matrix(estado, "Estado antes de MixColumns:")

    # Aplicar MixColumns
    new_state = mix_columns(t(estado))

    # Imprimir el estado después de MixColumns
    print_matrix(new_state, "Estado después de MixColumns:")

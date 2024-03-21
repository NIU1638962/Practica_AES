from AES_constants import S_BOX, RCON

def add_round_key(state, key):
    """Aplica la operación AddRoundKey al estado usando la clave de ronda dada."""
    for i in range(4):
        for j in range(4):
            state[i][j] ^= key[i][j]
    return state

def key_expansion(key):
    """Genera todas las claves de ronda a partir de la clave original para AES-128."""
    
    key_size = 16  # Tamaño de la clave en bytes
    exp_size = 176  # Tamaño total de la expansión de clave
    expanded_key = key[:]  # Comienza con la clave original
    
    rcon_iteration = 0
    while len(expanded_key) < exp_size:
        # Toma los últimos 4 bytes para la operación
        t = expanded_key[-4:]
        
        # Realiza una operación cada 16 bytes
        if len(expanded_key) % key_size == 0:
            # Rotación de byte
            t = t[1:] + t[:1]
            # S-Box y rcon
            t = [S_BOX[b] for b in t]
            t[0] ^= RCON[rcon_iteration]
            rcon_iteration += 1
        
        # XOR t con los 4 bytes 16 posiciones antes
        for i in range(4):
            if len(expanded_key) >= key_size:  # Comprobación de seguridad
                t[i] ^= expanded_key[-key_size + i]
        expanded_key.extend(t)
    
    # Convierte la clave expandida en una matriz de 4x4 para cada ronda
    round_keys = [expanded_key[i:i+16] for i in range(0, exp_size, 16)]
    return [ [ [round_key[i+j] for i in range(0, 16, 4)] for j in range(4) ] for round_key in round_keys ]



def xtime(a):
    """Realiza la multiplicación por {02} en GF(2^8)."""
    return (((a << 1) ^ 0x1B) if (a & 0x80) else (a << 1)) & 0xFF

def mix_single_column(a):
    """Aplica MixColumns a una única columna."""
    # a es una lista de 4 bytes (una columna del estado).
    t = a[0] ^ a[1] ^ a[2] ^ a[3]  # Total XOR de los 4 bytes
    u = a[0]  # Copia del primer byte
    for i in range(3):
        a[i] ^= t ^ xtime(a[i] ^ a[(i + 1) % 4])  # MixColumn operación
    a[3] ^= t ^ xtime(a[3] ^ u)
    return a

def mix_columns(state):
    """Aplica la operación MixColumns al estado completo."""
    for i in range(4):
        column = [state[j][i] for j in range(4)]  # Extrae la columna
        column = mix_single_column(column)
        for j in range(4):
            state[j][i] = column[j]  # Vuelve a insertar la columna mezclada
    return state

# Ejemplo de uso
state = [
    [0xdb, 0xf2, 0x01, 0xc6],
    [0x13, 0x0a, 0x01, 0xc6],
    [0x53, 0x22, 0x01, 0xc6],
    [0x45, 0x5c, 0x01, 0xc6]
]

print("Estado antes de MixColumns:")
for row in state:
    print(' '.join(format(x, '02x') for x in row))

# Aplica MixColumns
new_state = mix_columns(state)

print("\nEstado después de MixColumns:")
for row in new_state:
    print(' '.join(format(x, '02x') for x in row))





# Key_Expantion.py
from AES_constants_and_tools import S_BOX, RCON

def sub_word(word):
    """Aplica la S-Box a cada byte de una palabra."""
    return [S_BOX[b] for b in word]

def rot_word(word):
    """Realiza una rotación hacia la izquierda en una palabra."""
    return word[1:] + word[:1]

def key_expantion(key):
    key_size = 16  # Tamaño de clave para AES-128
    Nk = 4  # Número de palabras de 32 bits en la clave
    Nr = 10  # Número de rondas para AES-128
    expanded_key = key[:]  # Comienza con la clave original
    
    for i in range(Nk, 4 * (Nr + 1)):  # Expande hasta obtener 44 palabras de 32 bits
        temp = expanded_key[-4:]  # Última palabra
        if i % Nk == 0:
            temp = sub_word(rot_word(temp))  # Aplica RotWord y SubWord
            temp[0] ^= RCON[i // Nk - 1]  # Aplica XOR con el valor RCON adecuado
        # XOR de la palabra generada con la palabra 4 posiciones antes
        expanded_key += [temp[j] ^ expanded_key[-key_size + j] for j in range(4)]
    
    return expanded_key


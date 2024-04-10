from AES_constants_and_tools import CAD_DEBUG, KEY, print_matrix

def add_round_key(state, round_key):
    """Aplica la operación AddRoundKey al estado dado."""
    for i in range(4):
        for j in range(4):
            state[i][j] ^= round_key[i][j]
    return state

if __name__ == "__main__":
    # Usando CAD_DEBUG y KEY directamente desde el archivo auxiliar
    estado = CAD_DEBUG
     
    print_matrix(estado, "Estado sin cifrar:\n")
    
    # Imprimir la round_key
    print_matrix(KEY, "\nRound Key:\n")
    
    # Aplicar AddRoundKey
    new_state = add_round_key(estado, KEY)
    
    # Imprimir el estado después de AddRoundKey
    print_matrix(new_state, "\nEstado después de AddRoundKey:\n")

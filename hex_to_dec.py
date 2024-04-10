def decimal_to_hexadecimal(decimal_list):
    """
    Convierte una lista de valores decimales a sus equivalentes hexadecimales.
    
    Parámetros:
    - decimal_list: Lista de números decimales.
    
    Retorna:
    - Lista de cadenas representando los números en formato hexadecimal.
    """
    # Usa format() para convertir cada número decimal a hexadecimal, con dos dígitos.
    return [format(number, '02x') for number in decimal_list]

decimal_list = [22, 166, 136, 60]
hexadecimal_list = decimal_to_hexadecimal(decimal_list)
print(hexadecimal_list)

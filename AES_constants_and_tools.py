from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Configuración inicial
clave = bytes([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])

# Convertir CAD_DEBUG a bytes
CAD_DEBUG = [
    [0x32, 0x43, 0xf6, 0xa8],
    [0x88, 0x5a, 0x30, 0x8d],
    [0x31, 0x31, 0x98, 0xa2],
    [0xe0, 0x37, 0x07, 0x34]
]
CAD_DEBUG_flat = sum(CAD_DEBUG, [])  # Aplana la matriz
mensaje = bytes(CAD_DEBUG_flat)  # Convierte a bytes

# Cifrado con modo ECB
cipher = AES.new(clave, AES.MODE_ECB)
mensaje_cifrado = cipher.encrypt(pad(mensaje, AES.block_size))

# Convertir el mensaje cifrado a matriz de hexadecimales para imprimir
mensaje_cifrado_hex = [[f"{byte:02x}" for byte in mensaje_cifrado[i:i+4]] for i in range(0, len(mensaje_cifrado), 4)]

print("Mensaje Cifrado (como matriz hex):")
for row in mensaje_cifrado_hex:
    print(row)

# Descifrado con modo ECB
cipher_dec = AES.new(clave, AES.MODE_ECB)
mensaje_descifrado = unpad(cipher_dec.decrypt(mensaje_cifrado), AES.block_size)

# Convertir el mensaje descifrado a matriz para comparar con CAD_DEBUG
mensaje_descifrado_matriz = [[mensaje_descifrado[i*4 + j] for j in range(4)] for i in range(4)]

print("\nMensaje Descifrado (como matriz):", mensaje_descifrado_matriz)

# Verificar si es igual a CAD_DEBUG
if mensaje_descifrado_matriz == CAD_DEBUG:
    print("\nEl mensaje descifrado coincide con CAD_DEBUG")
else:
    print("\nEl mensaje descifrado NO coincide con CAD_DEBUG")

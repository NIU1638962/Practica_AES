from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Configuración inicial
CAD = "JoelT AlejandroJ"  # Mensaje a cifrar
clave = bytes([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])  # Clave de 16 bytes

# Mensaje para cifrar
mensaje = CAD.encode()  # Codifica la cadena CAD a bytes

# Cifrado con modo ECB
cipher = AES.new(clave, AES.MODE_ECB)
mensaje_cifrado = cipher.encrypt(pad(mensaje, AES.block_size))  # Añade padding al mensaje y luego lo cifra

print("Mensaje Cifrado (en bytes):", mensaje_cifrado)

# Descifrado con modo ECB
cipher_dec = AES.new(clave, AES.MODE_ECB)  # Se debe usar la misma clave para el descifrado
mensaje_descifrado = unpad(cipher_dec.decrypt(mensaje_cifrado), AES.block_size)  # Descifra y elimina el padding

print("Mensaje Descifrado (string):", mensaje_descifrado.decode())  # Decodifica de bytes a string

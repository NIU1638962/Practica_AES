from Crypto.Cipher import AES
import binascii

# Clave proporcionada convertida a bytes
key_hex = '2b2878097eaef7cf15d2154f16a6883c'
key = binascii.unhexlify(key_hex)

# Texto proporcionado convertido a bytes
texto = "JoelT AlejandroJ".ljust(16)[:16]  # Asegura que tiene exactamente 16 caracteres
texto_bytes = texto.encode()  # Codifica el texto a bytes

# Inicializa el cifrador AES con la clave y el modo ECB
cipher = AES.new(key, AES.MODE_ECB)

# Cifra el texto
ciphertext = cipher.encrypt(texto_bytes)

# Imprime el texto cifrado en formato hexadecimal
print("Texto cifrado (hex):", binascii.hexlify(ciphertext).decode())

# Ahora, compara este resultado con el que obteniste de tu función `cifrar_aes`.
# Recuerda que debes convertir el resultado de tu función `cifrar_aes` a formato hexadecimal para una comparación adecuada.
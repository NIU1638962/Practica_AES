# Lista de archivos para concatenar
files_to_concatenate = [
    "ShiftRows.py",
    "AddRoundKey.py",
    "AES.py",
    "AES_constants_and_tools.py",
    "ByteSub.py",
    "Key_Expantion.py",
    "MixColumns.py"
]

# Nombre del archivo de salida
output_file_name = "concatenated_files.txt"

# Abrir el archivo de salida en modo de escritura
with open(output_file_name, "w") as output_file:
    # Iterar sobre cada archivo de la lista
    for file_name in files_to_concatenate:
        # Intentar abrir el archivo actual
        try:
            with open(file_name, "r") as current_file:
                # Escribir un encabezado para identificar el archivo actual
                output_file.write(f"{'='*20}\n{file_name}\n{'='*20}\n\n")
                
                # Leer el contenido del archivo actual y escribirlo en el archivo de salida
                output_file.write(current_file.read())
                
                # Escribir una nueva línea después de cada archivo para separación
                output_file.write("\n\n")
        except FileNotFoundError:
            print(f"El archivo {file_name} no fue encontrado y será omitido.")

print(f"Todos los archivos han sido concatenados en {output_file_name}.")

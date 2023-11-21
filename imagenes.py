def encrypt_image(image_path, key):
    try:
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        
        # Convertir la clave a bytes si es una cadena
        if isinstance(key, str):
            key = key.encode()

        # Convertir la imagen a una lista de bytes
        byte_data = bytearray(image_data)

        # Encriptar la imagen byte a byte utilizando XOR
        for i, byte in enumerate(byte_data):
            byte_data[i] = byte ^ key[i % len(key)]

        # Guardar la imagen encriptada en un nuevo archivo
        encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'  # Cambiar la extensión según la imagen
        with open(encrypted_image_path, 'wb') as encrypted_image_file:
            encrypted_image_file.write(byte_data)

        print("Imagen encriptada y guardada como:", encrypted_image_path)
        return encrypted_image_path
    
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None

def decrypt_image(encrypted_image_path, key):
    try:
        with open(encrypted_image_path, 'rb') as encrypted_image_file:
            encrypted_data = encrypted_image_file.read()
        
        # Convertir la clave a bytes si es una cadena
        if isinstance(key, str):
            key = key.encode()

        # Convertir los datos encriptados a una lista de bytes
        byte_data = bytearray(encrypted_data)

        # Desencriptar la imagen byte a byte utilizando XOR
        for i, byte in enumerate(byte_data):
            byte_data[i] = byte ^ key[i % len(key)]

        # Guardar la imagen desencriptada en un nuevo archivo
        decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'  # Cambiar la extensión según la imagen
        with open(decrypted_image_path, 'wb') as decrypted_image_file:
            decrypted_image_file.write(byte_data)

        print("Imagen desencriptada y guardada como:", decrypted_image_path)
        return decrypted_image_path
    
    except FileNotFoundError:
        print("Archivo no encontrado.")
        return None

# Ejemplo de uso
image_path = 'ruta_de_tu_imagen.png'  # Reemplaza con la ruta de tu imagen
key = 'SECRET'  # Puede ser cualquier cadena de caracteres

# Encriptar la imagen
encrypted_path = encrypt_image(image_path, key)

# Desencriptar la imagen
if encrypted_path:
    decrypted_path = decrypt_image(encrypted_path, key)
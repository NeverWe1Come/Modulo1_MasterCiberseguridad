#!/usr/bin/env python
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64

#Declaración de las variables globales en Python
message = "a secret message"
key = "12345678901234567890123456789012"

#Conversión de variables
def variables_bytes():
    #Convierto la frase a encriptar en bytes
    message_bytes = message.encode()
    #Convierto la frase a encriptar en bytes
    key_bytes = key.encode()
    #Devuelvo las variables en un diccionario
    global diccionario
    diccionario = {'mensaje_bytes':message_bytes,'clave_base64':key_bytes,'bloque':os.urandom(16)}

#Creación Cipher de froma global para usarlo en el resto de funciones
def crear_cipher(clave_base64,bloque):
    global cipher
    cipher = Cipher(algorithms.AES(clave_base64), modes.CBC(bloque))

#Función encripta el mensaje original
def encriptar_CBC():
    #Llamo a la variable cipher y encripto el mensaje
    encryptor = cipher.encryptor()
    ct = encryptor.update(diccionario['mensaje_bytes']) + encryptor.finalize()
    return ct

#Función desencripta el emnsaje con la clave propio
def desencriptar_CBD(mensaje_encriptado):
    # Llamo a la variable cipher y desencripto el mensaje.
    decryptor = cipher.decryptor()
    aux = decryptor.update(mensaje_encriptado) + decryptor.finalize()
    print('MENSAJE DESENCRIPTADO: ' + aux.decode('utf-8'))
    return aux

#Función main que llama a todos los métodos necesarios
if __name__ == '__main__':
    variables_bytes()
    crear_cipher(diccionario['clave_base64'],diccionario['bloque'])
    message_encriptado = encriptar_CBC()
    desencriptar_CBD(message_encriptado)
#!/usr/bin/env python
import os
from cryptography.fernet import Fernet
import base64

#Declaración de las variables globales en Python
message = "a secret message"
key = "12345678901234567890123456789012"

#Conversión de variables
def variables_bytes_b64():
    #Convierto la frase a encriptar en bytes
    message_bytes = message.encode()
    # Primero convierto la frase a encriptar en bytes y despues la codifico en base64
    key_b64 = base64.b64encode(key.encode())
    #Devuelvo las variables en un diccionario
    global diccionario
    diccionario = {'mensaje_bytes':message_bytes,'clave_base64':key_b64}

#Creación variable de Fernet del módulo Cryptography
def usar_fernet(key_b64):
    f = Fernet(key_b64)
    return f;

#Función encripta el mensaje original
def encriptar_CBC(mensaje_bytes):
    #Llamo a la variable de fernet para encriptar, con la clave introducida, que se encuentra en el diccionario
    token = usar_fernet(diccionario['clave_base64']).encrypt(mensaje_bytes)
    print('MENSAJE ENCRIPTADO: ' + token.decode('utf-8'))
    return token

#Función desencripta el emnsaje con la clave propio
def desencriptar_CBD(mensaje_encriptado):
    # Llamo a la variable de fernet para desencriptar, con la clave introducida, que se encuentra en el diccionario
    token2 = usar_fernet(diccionario['clave_base64']).decrypt(mensaje_encriptado)
    print('MENSAJE DESENCRIPTADO: ' + token2.decode('utf-8'))
    return token2

#Función main que llama a todos los métodos necesarios
if __name__ == '__main__':
    variables_bytes_b64()
    message_encriptado = encriptar_CBC(diccionario['mensaje_bytes'])
    desencriptar_CBD(message_encriptado)
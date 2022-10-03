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
def crear_ciphers(key_b64,iv):
    global diccionario_ciphers
    cipher_OFB = Cipher(algorithms.AES(key_b64), modes.OFB(iv))
    cipher_CFB = Cipher(algorithms.AES(key_b64), modes.CFB(iv))
    cipher_ECB = Cipher(algorithms.AES(key_b64), modes.ECB())
    diccionario_ciphers = {'cipher_OFB':cipher_OFB,'cipher_CFB':cipher_CFB,'cipher_ECB':cipher_ECB}

#Función encripta el mensaje original
def encriptar_CBC():
    #Llamo a la variable cipher y encripto el mensaje
    encryptor_OFB = diccionario_ciphers['cipher_OFB'].encryptor()
    encryptor_CFB = diccionario_ciphers['cipher_CFB'].encryptor()
    encryptor_ECB = diccionario_ciphers['cipher_ECB'].encryptor()
    ct1 = encryptor_OFB.update(diccionario['mensaje_bytes']) + encryptor_OFB.finalize()
    ct2 = encryptor_CFB.update(diccionario['mensaje_bytes']) + encryptor_CFB.finalize()
    ct3 = encryptor_ECB.update(diccionario['mensaje_bytes']) + encryptor_ECB.finalize()
    diccionario_encryptor = {'ct1':ct1,'ct2':ct2,'ct3':ct3}
    return diccionario_encryptor

#Función desencripta el emnsaje con la clave propio
def desencriptar_CBD(diccionario_encryptor):
    print(diccionario_encryptor)
    # Llamo a la variable cipher y desencripto el mensaje.
    decryptor1_OFB = diccionario_ciphers['cipher_OFB'].decryptor()
    decryptor2_CFB = diccionario_ciphers['cipher_CFB'].decryptor()
    decryptor3_ECB = diccionario_ciphers['cipher_ECB'].decryptor()
    aux1_OFB = decryptor1_OFB.update(diccionario_encryptor['ct1']) + decryptor1_OFB.finalize()
    aux2_CFB = decryptor2_CFB.update(diccionario_encryptor['ct2']) + decryptor2_CFB.finalize()
    aux3_ECB = decryptor3_ECB.update(diccionario_encryptor['ct3']) + decryptor3_ECB.finalize()
    print('MENSAJE DESENCRIPTADO: ' + aux1_OFB.decode('utf-8'))
    print('MENSAJE DESENCRIPTADO: ' + aux2_CFB.decode('utf-8'))
    print('MENSAJE DESENCRIPTADO: ' + aux3_ECB.decode('utf-8'))


#Función main que llama a todos los métodos necesarios
if __name__ == '__main__':
    variables_bytes()
    crear_ciphers(diccionario['clave_base64'],diccionario['bloque'])
    diccionario_mensajes_encriptados = encriptar_CBC()
    desencriptar_CBD(diccionario_mensajes_encriptados)
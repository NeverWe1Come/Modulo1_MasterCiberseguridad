#!/usr/bin/env python
import os
from cryptography.hazmat.primitives import hashes
import binascii

hash_md5_fichero_original = '944a1e869969dd8a4b64ca5e6ebc209a'
ruta_fichero1= './WinMD5.exe'
ruta_fichero2= './WinMD5_2.exe'
#Función main que llama a todos los métodos necesarios

def calcular_MD5(ruta_fichero):
    #Abro el fichero solo de lectura r y binario b (Con ello obtenemos los bytes del fichero)
    archivo = open(ruta_fichero, 'rb')
    #Lee el fichero y almaceno los bytes en la variable buffer
    buffer = archivo.read()
    #Utilizo la librería Cryptography para calcular el hash MD5 del fichero
    digest = hashes.Hash(hashes.MD5())
    digest.update(buffer)
    #Almaceno en la variable aux el hash del fichero
    aux = digest.finalize()
    #Utilizo la libreria Binascii, para convertir la salida en bytes a hexadecimal y más tarde a str
    hash_final = binascii.hexlify(aux).decode('utf-8')
    print('El hash MD5 del fichero ' +ruta_fichero+ ' es: ' + hash_final)
    return hash_final

if __name__ == '__main__':
    hash_fichero1 = calcular_MD5(ruta_fichero1)
    hash_fichero2 = calcular_MD5(ruta_fichero2)

    if(hash_fichero1 == hash_md5_fichero_original):
        print('El fichero correcto es: ' + ruta_fichero1)
    elif (hash_fichero2 == hash_md5_fichero_original):
        print('El fichero correcto es: ' + ruta_fichero2)
    else:
        print('Ninguno de los dos es correcto')
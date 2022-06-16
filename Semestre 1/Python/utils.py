import hashlib
import getpass
import time

def cifrar (entrada):
    entrada_binaria=entrada.encode('ascii')
    resultado = hashlib.md5(entrada_binaria)
    return (resultado.hexdigest())


def obtener_calve(mensaje):
    pswd = getpass.getpass(mensaje+": ")
    return (pswd)
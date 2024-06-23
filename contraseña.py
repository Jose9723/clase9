import random

def generar_contraseña(longitud):
    caracteres = "abcdefghijkmnñopqrstuvwxyzABCDEFGHIJKMNÑOPQRSTUVWXYZ123456789!@#$%&"
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña
def main():
    while True:
       longitud = int(input("ingresa la longitud que quieras para la contraseña: "))     
       contraseña  = generar_contraseña(longitud)
       print ("La contraseña generada es:", contraseña)
    
main()
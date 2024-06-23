import random

def generar_contraseña(longitud):
    if longitud < 8:
        raise ValueError("La longitud de la contraseña debe ser al menos 8 caracteres.")
    
    caracteres = "abcdefghijkmnñopqrstuvwxyzABCDEFGHIJKMNÑOPQRSTUVWXYZ123456789!@#$%&"
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña 
def main():
    while True:
        try:
            longitud = int(input("Ingresa la longitud que quieras para la contraseña: "))     
            contraseña  = generar_contraseña(longitud)
            print("La contraseña generada es:", contraseña)
        except ValueError as e:
          print(f"Error: {e}")
          
main()

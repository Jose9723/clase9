import random

def tirar_dados(numero_de_dados):
    resultados = []
    for _ in range(numero_de_dados):
        resultado_dado = random.randint(1, 6)
        resultados.append(resultado_dado)
    return resultados

def main():
   while True: 
    try:
       num_dados = int(input("¿Cuántos dados quieres lanzar? "))
       if num_dados <= 0:
        print("Debe ingresar un número mayor que cero.")
       else:
          resultados = tirar_dados(num_dados)
        
          print("Resultados de los dados:")
          for i, resultado in enumerate(resultados):
            print(f"Dado {i + 1}: {resultado}")
            
    except ValueError:
          print("Ingrese un número entero válido.")

main()
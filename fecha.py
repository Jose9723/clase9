import datetime

fecha_nacimiento = input("Ingrese tu fecha de nacimiento (DD MM AAAA): ")
fecha = datetime.datetime.strptime(fecha_nacimiento,"%d %m %Y")
dias_semana =["Lunes","Martes","Miercoles","Jueves","Viernes","Sábado","Domingo"]
dia_semana = dias_semana[fecha.weekday()]
print(f"Naciste un {dia_semana}.")
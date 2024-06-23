import calendar 
 
print()

import calendar

def mostrar_calendario_con_fecha():
    while True:
        fecha_str = input("Ingrese una fecha en formato DD MM AAAA: ")
        try:
            dia, mes, anio = map(int, fecha_str.split(' '))
            if not (1 <= mes <= 12 and 1 <= dia <= calendar.monthrange(anio, mes)[1]):
                raise ValueError("Fecha no válida.")
            break
        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo.")

    cal = calendar.monthcalendar(anio, mes)
    nombre_mes = calendar.month_name[mes]

    
    print(f"\nCalendario de {nombre_mes} {anio}:")
    print("Lun  Mar  Mié  Jue  Vie  Sáb  Dom")
    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end=" ")
            elif day == dia:
                print(f" [{day:2d}]", end=" ")
            else:
                print(f" {day:2d} ", end=" ")
        print()

mostrar_calendario_con_fecha()

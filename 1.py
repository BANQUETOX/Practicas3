# A usted le piden realizar un programa que, recibiendo el día, el mes y el año de la fecha de hoy, calcule e imprima
# la fecha del día de mañana.

def calc_tomorrow(day, month, year):
    if month == "diciembre":
        if day > 31:
            print("Fecha invalida")
        elif day == 31:
            day = 1
            year += 1
        else:
            day += 1
            print(f"Mañana es {day} de {month} del {year}")

    elif month == "febrero":
        if day > 28:
            print("Fecha invalida")
        elif day == 28:
            day = 1
            month = "marzo"
        else:
            day += 1
            print(f"Mañana es {day} de {month} del {year}")

    elif month == "enero" or "marzo" or "mayo" or "agosto" or "octubre":
        if day > 31:
            print("Fecha invalida")
        elif day == 31:
            day = 1
            if month == "enero":
                month = "febrero"
            elif month == "marzo":
                month = "abril"
            elif month == "mayo":
                month == "junio"
            elif month == "agosto":
                month = "septiembre"
            elif month == "octubre":
                month = "noviembre"
            print(f"Mañana es {day} de {month} del {year}")
        else:
            day += 1
            print(f"Mañana es {day} de {month} del {year}")
    else:
        if day > 30:
            print("Fecha invalida")
        elif day == 30:
            day = 1
            if month == "abril":
                month = "mayo"
            elif month == "junio":
                month = "julio"
            elif month == "septiembre":
                month == "octubre"
            elif month == "noviembre":
                month = "diciembre"
            print(f"Mañana es {day} de {month} del {year}")
        else:
            day += 1
            print(f"Mañana es {day} de {month} del {year}")


day = int(input("Que dia es hoy"))
month = input("En que mes estamos?").lower()
year = int(input("En que año estamos?"))

calc_tomorrow(day, month, year)

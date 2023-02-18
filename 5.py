# La escuela centroamericana de geología de la UCR desea fortalecer sus herramientas de estudio petrológicas, y
# para eso solicita su ayuda. Desea que usted le haga un programa que lea la edad aproximada de una piedra y
# calcule cuál es la era geológica en la que se originó. Una era geológica simplemente es un periodo de tiempo,
# usualmente de varios millones de años, donde se realizaron cierto tipo de procesos geológicos. Particularmente,
# para la formación de Costa Rica nos interesan 4 eras: cenozoica, mesozoica, paleozoica y pre-paleozoica. Una
# piedra con menos de 65.5 millones de años de haber sido formada pertenece a la era cenozoica. Una con más de
# esta cantidad, pero menos de 251 millones de años se clasifica como mesozoica. Una con más de esta edad,
# pero menos de 542 millones de años se considera de la era paleozoica. Una piedra con más de esta cantidad de
# años se considera como de la era pre-paleozoica. El siguiente cuadro resume esta información:

# Edad de la piedra (en millones de años)
#   Cenozoica     Mesozoica    Paleozoica    Pre-paleozolica
#    < 65.5         < 251        < 542       >= 542


def stone_age(age):
    if age < 65.5:
        print("Es de la edad Cenozoica")
    elif age < 251:
        print("Es de la edad Mesozoica")
    elif age < 542:
        print("Es de la edad Paleozoica")
    elif age >= 542:
        print("Es de la edad Pre-paleozolica")
    else: 
        print("Datos invalidos")

age = float(input("Cuantos a;os de antiguedad tiene la piedra? "))
stone_age(age)
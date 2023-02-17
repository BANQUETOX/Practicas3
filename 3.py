# A usted se le pide realizar un programa que determine si un estudiante de una institución universitaria es candidato
# a que le den una beca. Un estudiante puede optar por una beca solamente si lleva el bloque de cuatro materias
# completo, y no perdió ninguna materia, por lo que el ##sistema siempre va a recibir las notas de las cuatro materias y
# todas las notas van a ser superiores a 70##. El estudiante tiene derecho a la beca si ###el promedio de las notas de las
# materias del cuatrimestre es igual o superior a noventa###, y ##si ninguna nota está por debajo de 8. También podría
# tener derecho a la beca si el promedio de las materias del cuatrimestre es igual a superior a 85###, fue asistente
# durante el cuatrimestre y la calificación que se le otorgó como asistente fue de una A o una B. Si su calificación
# como asistente fue de una C no tiene derecho a beca, sin importar el promedio.

def scolarship(first_subject, second_subject, third_subject, fourth_subject):
    grades = [first_subject , second_subject , third_subject , fourth_subject]
    average = (grades[0] + grades[1] + grades[2] + grades[3]) / len(grades)
    if average >= 90:
        print("Es elejible para la beca")
    else:
        for grade in grades: 
            if grade < 80:
                print("No es elejible para la beca")
                break
            else:
                assist_help = input("Fue asistente durante el cuatrimestre? si/no ").lower()
                if assist_help == "no":
                    print("No es elejible para la beca")
                    break
                else:
                    assist_grade = input("Que calificacion recibio por su ayuda? a/b/c ").lower()
                    if assist_grade == "a" or assist_grade == "b":
                        print("Es elejible para la beca")
                        break
                    else:
                         print("No es elejible para la beca")
                         break
                         

            
        
scolarship(float(input("Nota de la primera materia ")),float(input("Nota de la segunda materia ")), float(input("Nota de la tercera materia ")), float(input("Nota de la cuarta materia ")))

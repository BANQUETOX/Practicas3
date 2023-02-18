# El operador de telefonía móvil principal de la cuidad, decidió realizar una promoción basada en el monto de la
# recarga que realice el cliente y en los años que tiene de utilizar los servicios del operador. El operador no acepta
# recargas inferiores a los dos mil colones ni mayores a 5000. Si el cliente tiene menos de un año de estar registrado
# con el operador, no participa en la promoción. Si la recarga es mayor o igual a 2000 colones, pero menor a 3800, y
# tiene un año y hasta no más de 3 años de estar registrado con el operador, se le duplica la recarga. Para todos los
# clientes que tengan más de tres y no más de 5 años y la recarga sea mayor o igual a 3 800 colones y hasta un
# máximo de 5000 mil colones, se le triplica la recarga. Para los clientes que tienen más de cinco años, sin importar
# el monto de la recarga, se les triplica la misma. Haga un programa que reciba el nombre del cliente, el monto de la
# recarga y la cantidad de años que tienen de ser cliente, y retorne si le aplica o no la promoción, y el monto total de
# la recarga incluyendo la promoción.

#input (nombre, monto de recarga, a;os)
#returns (if aplicant, mount-recharge)

def recharge(name,amount, years):
    max_amount = 5000
    min_amount = 2000
    final_recharge = amount

    if amount > max_amount or amount < min_amount:
        print("Monto de recarga invalido")
    else:
        print("Calculando costes...")
        
        if years < 1:
            print("Lo sentimos no participa en la promocion")
        elif years > 5:
            print("Felicidades su recarga se ha triplicado!!!")
            final_recharge *= 3
        elif years > 2 and years <= 5:
            if amount > 3800 and amount <= max_amount:
             print("Felicidades su recarga se ha triplicado!!!")
             final_recharge *= 3
        elif years < 4:
            if amount >= min_amount and amount < 3800:
             print("Felicidades su recarga se ha duplicado!!!")
             final_recharge *= 2
        else:
            print("Datos invalidos")
        print(f"Usted recivio {final_recharge} de recarga, a un coste de {amount} ")
    
    

name = input("Cual es su nombre? ")
amount = float(input("Cuanto desea recargar? "))
years = int(input("Cuantos años lleva usando nuestros servicios? "))

recharge(name, amount, years)
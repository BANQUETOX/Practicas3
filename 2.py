#A usted se le pide que realice un programa que, recibiendo la medida de tres lados, se imprima si estos tres lados
# pueden formar un triángulo. Tres lados forman un triángulo si la suma de dos lados de un triángulo siempre es
# mayor al tercer lado. Por ejemplo, si tenemos un lado a que mide 7, un lado b que mide 10 y un lado c que mide 5,
# se compara si la suma de los lados b y c es mayor que la medida del lado a. Luego si la suma de los lados a y b es
# mayor que la medida del lado c y, finalmente, si la suma del lado a y c es mayor que la medida del lado b. Si las
# tres condiciones se cumplen, entonces los tres lados conforman un triángulo.

def triangle(first_side, second_side, third_side):
    if second_side + third_side > first_side and first_side + second_side > third_side and first_side + third_side > second_side:
        print("Si puede ser un triangulo")
    else:
        print("No puede ser un triangulo")

triangle(float(input("Cuanto mide el primer lado?")), float(input("Cuanto mide el segundo lado?")), float(input("Cuanto mide el tercer lado?")))
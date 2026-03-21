#Algoritmo consumo de agua
#pedir al usuario que ingrese su nombre
#Pedir al usuario que ingrese su consumo mensual de agua en metros cúbicos
#Mostrar en consola el nombre del usuario, la categoría y el mensaje correspondiente.
#Si el consumo es 0 o negativo, mostrar el mensaje de error correspondiente

nombre=input("ingrese su nombre: ")
print("Hola",nombre)
consumo=int(input("ingrese su consumo mensual de agua en metros cubicos(numero entero)"))

if consumo >= 1 and consumo <= 15:
    print(nombre,"tienes Bajo consumo","¡Excelente! Eres un usuario responsable del agua")
elif consumo > 15 and consumo <= 30:
    print(nombre,"tienes Consumo normal","Tu consumo está dentro del promedio del hogar")
elif consumo > 30:
    print(nombre,"tienes Alto consumo","Atención: tu consumo es alto, revisa posibles fugas")
else:
    print("Dato inválido, Error: el consumo debe ser mayor a 0")

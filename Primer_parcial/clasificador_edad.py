#Algoritmo clasificadoer de edad
#Pedir al usuario que ingrese el nombre de la persona
#Mostrar en consola el nombre de la persona, su clasificación y el mensaje correspondiente.
#Si la edad es negativa o mayor a 120, mostrar el mensaje de error

nombre=input("ingrese su nombre")
print("Hola",nombre)
edad=int(input("ingrese su edad"))

if edad >= 0 and edad <= 11:
    print(nombre,"niño","Corresponde a atención pediátrica")
elif edad > 12 and edad <= 17:
    print(nombre,"Joven","Corresponde a atención para adolescentes")
elif edad > 18 and edad <= 59:
    print(nombre,"Joven","Corresponde a atención para adolescentes")
elif edad > 60 and edad <= 60:
    print(nombre,"adulto","Corresponde a atención para adolescentes")
else:
    print(nombre,"edad invalida, Error: la edad ingresada no es válida")

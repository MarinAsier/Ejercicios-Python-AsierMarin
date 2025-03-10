# coding=utf-8
#Pide la edad y el nombre por teclado. En caso de ser mayor de 18 años indica que ya puede conducir.
def mayor_edad(e):
    return e>=18

# Programa principal
def main():
    nombre=input("Introduce tu nombre: ")
    edad=int(input("Introduce tu edad: "))

    if mayor_edad(edad):
        print(nombre,"ya puede conducir")
    else:
        print(nombre,"no puede conducir")

    # Utilice la función definida
    # Estructura alternativa Si (condidición con función) entonces --> sino ...

if __name__== "__main__" :
   main()

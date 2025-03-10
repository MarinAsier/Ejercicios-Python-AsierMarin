# coding=utf-8
__Author__="Asier Marin Saez"

def suma(x,y) :
    return x + y

def resta(x,y) :
    return x - y

def multiplica(x,y) :
    return x * y

def divide(x,y) :
    if y == 0 :
        print("Error: No se puede dividir por cero.")
    return x / y

# Función que crea el menú de la aplicacion.

def menuApp() :
    print("MENU CALCULADORA")
    opcion =-1

    while opcion !=0 :
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("0. Salir")

        opcion=int(input("Introduzca opción: "))

        if opcion == 1 :
            s1=int(input("Introduzca el primer sumando: "))
            s2=int(input("Introduzca el segundo sumando: "))
            print("La suma de {0} + {1} = {2}.\n".format(s1,s2,suma(s1,s2)))

        elif opcion == 2 :
            minuendo=int(input("Introduzca el minuendo: "))
            sustraendo=int(input("Introduzca el sustraendo: "))
            print("La resta de {0} - {1} = {2}.\n".format(minuendo,sustraendo,resta(minuendo,sustraendo)))

        elif opcion == 3 :
            m1 = float(input("Introduzca el primer factor: "))
            m2 = float(input("Introduzca el segundo factor: "))
            print("La multiplicación de {0} * {1} = {2}.\n".format(m1,m2,multiplica(m1,m2)))

        elif opcion == 4 :
            d1 = float(input("Introduzca el dividendo: "))
            d2 = float(input("Introduzca el divisor: "))
            print("La división de {0} / {1} = {2}.\n".format(d1,d2,divide(d1,d2)))

        elif opcion == 0 :
            print("Saliendo de la aplicación...")
            break
        else :
            print("\nError: Opción incorrecta, introduzca una nueva opción.")

# Programa principal
def main():
    menuApp()
    

if __name__== "__main__" :
   main()

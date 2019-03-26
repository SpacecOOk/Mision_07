#Autor: Michel Antoine Dionne Gutierrez A0174863, Grupo: 03
#Ciclos While


def dividir(divisor, dividiendo):
    contador = 0
    while divisor >= dividiendo:
        divisor = divisor - dividiendo
        contador = contador + 1
    print(divisor,"/",dividiendo,"=",contador,"y sobran",divisor)


def econtrarMayor():
    numero = int(input("Teclea un numero[teclea -1 para salir ]"))
    mayor = 0
    if numero != -1:
        while numero != -1:
            if numero >= 0:
                if numero >= mayor:
                    mayor = numero
            numero = int(input("Teclea un numero[teclea -1 para salir ]"))
        print(mayor)
    else:
        print("No hay valor mayor")


def main():
    print(""" Mission 07. Ciclos while
              Autor: Michel ANtoine Dionne Gutierrez
              Matricula: A01748632
              1.- calcular divisiones
              2.- encuentra el mayor
              3.- salir
              Teclea tu opcion:""")
    opcion = int(input("Teclea tu opcion"))
    while opcion != 3:
        if opcion == 1:
            divisor = int(input("Teclea el numero que quieres dividir"))
            dividiendo = int(input("Teclea el numero por el cual quieres dividir"))
            dividir(divisor,dividiendo)
        elif opcion == 2:
            print("Teclea una serie de valores para encontrar el mayor")
            econtrarMayor()
        elif opcion > 3:
            print("ERROR ,solo valores del 1 al 3")
        opcion = int(input(""" Mission 07. Ciclos while
              Autor: Michel ANtoine Dionne Gutierrez
              Matricula: A01748632
              1.- calcular divisiones
              2.- encuentra el mayor
              3.- salir
              Teclea tu opcion:"""))
    print("Gracias por usar este programa, vuelva pronto")



main()

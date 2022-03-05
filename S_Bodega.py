import random
import time
vasos=["vasos",random.randint(300,500)]
cucharas=["cucharas",random.randint(300,500)]
cuchillos=["cuchillos",random.randint(300,500)]
tenedores=["tenedores",random.randint(300,500)]
productos=[vasos,cucharas,cuchillos,tenedores]
ncant=[]
def sumrest():
    op=input("Si desea restar un producto ingrese'restar',\nSi desea sumar ingrese sumar'").upper()
    if op=="RESTAR":
        rpro=input("Cuál producto desea restar?").upper()
        if rpro=="VASOS":
            res=int(input("Ingrese las unidades que desea restar "))
            print(vasos)
            vasos[-1]=vasos[-1]-res
            print(vasos)
        if rpro=="CUCHARAS":
            res=int(input("Ingrese las unidades que desea restar "))
            cucharas[-1]=cucharas[-1]-res
        if rpro=="CUCHILLOS":
            res=int(input("Ingrese las unidades que desea restar "))
            cuchillos[-1]=cuchillos[-1]-res
        if rpro=="TENEDORES":
            res=int(input("Ingrese las unidades que desea restar "))
            tenedores[-1]=tenedores[-1]-res
    else:
        rpro=input("Cuál producto desea sumar? ").upper()
        if rpro=="VASOS":
            summ=int(input("Ingrese las unidades que desea sumar "))
            vasos[-1]=vasos[-1]+summ
        if rpro=="CUCHARAS":
            summ=int(input("Ingrese las unidades que desea sumar "))
            cucharas[-1]=cucharas[-1]+summ
        if rpro=="CUCHILLOS":
            summ=int(input("Ingrese las unidades que desea sumar "))
            cuchillos[-1]=cuchillos[-1]+summ
        if rpro=="TENEDORES":
            summ=int(input("Ingrese las unidades que desea sumar "))
            tenedores[-1]=tenedores[-1]+summ
def newprod(nombre,cant):
    nuevop=[]
    nuevop=[nombre,cant]
    productos.append(nuevop)
def quitar(nomb):
    del productos[nomb]
def bodega():
    #menu
    print("Control de Bodega")
    print("Si agregar o restar stock, indique 1")
    print("Si agregar productos, indique 2")
    print("Si desea quitar productos, indique 3")
    print("Si desea ver todos los productos, indique 4")
    print("Si desea verificar stock, indique 5")
    opcionmenu = int(input("Ingrese su opcion: "))
    if opcionmenu==1:
        sumrest()
    elif opcionmenu==2:
        nombre=input("Ingrese el nombre del nuevo producto: ").capitalize()
        cant=int(input("Ingrese las unidades de este nuevo producto: "))
        newprod(nombre,cant)
        print(productos)
    elif opcionmenu==3:
        print("Si desea eliminar los vasos, indique 0")
        print("Si desea eliminar los cucharas, indique 1")
        print("Si desea eliminar los cuchillos, indique 2")
        print("Si desea eliminar los tenedores, indique 3")
        print("Si desea eliminar el producto agregado, indique 4")
        nombr=int(input("Ingrese el número del producto a eliminar: "))
        quitar(nombr)
        print(productos)
    elif opcionmenu==4:
        for prod in productos:
            print(prod)
            time.sleep(1)
    elif opcionmenu==5:
        for producto in productos:
            # print(producto)
            for cantidad in range(1,len(producto),2):
                # print(producto[cantidad])
                if cantidad<400:
                    print("Quedan menos de 400 unidades de",producto[0])
boocle=False
while not boocle:
    boocle=bodega()
    salir=input("Ingrese 'salir' si desea terminar el programa,sino ingrese cualquier tecla: ").upper()
    if salir=="SALIR":
        print("Nos vemos")
        break
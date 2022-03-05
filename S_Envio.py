import random

#Este es el sistema de envio de la empresa Te lo Vendo
print("PROGRAMA PARA VERIFICAR QUE TIPO DE ENVIO SE NECESITA Y QUE BODEGA SE ENVIA")

producto = input("Ingrese producto")
cantidad = random.randint(1,200)
stock_bodegaa = random.randint(1,500)
stock_bodegab = random.randint(1,500)
BODEGA_A = []
BODEGA_B = []

def dondeenviar(envio):
    if envio >= 1000:
        print("En envio tiene más de 1000 km, por tanto es un envio lento")
        distancia = "largo"
    if envio <1000:
        print("El envio tiene menos de 1000 km, por lo tanto es un envio rápido")
        distancia = "corto"
    print(envio)
    return distancia

def enviobodega(tipo_envio):
    if tipo_envio == "corto" and (stock_bodegaa + cantidad) <= 500:
        BODEGA_A.append(producto)
        newstock = stock_bodegaa + cantidad
        BODEGA_A.append(newstock)
        print("Enviado a Bodega A, stock bodega:", BODEGA_A)
        
    if tipo_envio == "largo"and (stock_bodegab + cantidad) <=500:
        BODEGA_B.append(producto)
        newstock = stock_bodegaa + cantidad
        BODEGA_B.append(newstock)
        print("Enviado a Bodega B, stock bodega:", BODEGA_B)
    else: print("No hay capacidad para mas material")

envio = int(input("A cuanta distancia en km hay que enviar el producto"))
print(type(envio))
tipo_envio = dondeenviar(envio)
comprobar = ""
enviobodega(tipo_envio)

print("\nStock inicial bodega A", stock_bodegaa)
print("Nuevos productos en Bodega A:", BODEGA_A)

print("\nStock inicial bodega", stock_bodegab)
print("Nuevos productos Bodega B:", BODEGA_B)




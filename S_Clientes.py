#Variable de Clientes
listaClientes=[
    [0,1,2,3,4],
    ['nombre', 'Ian','Felipe','Camila','Anibal'],
    ['apellidos','Hernandez','Godoy','Pedraza','Reinoso'],
    ['edad', '27','28','22','35'],
    ['contraseñas', 'Contraseña1','Contraseña2','Contraseña3','Contraseña4']
]
#Funciones
#Agregar clientes nuevos
def clienteNuevo(Nombre,Apellido,edad):
    idAutomatico=max(listaClientes[0])+1
    listaClientes[0].append(idAutomatico)
    listaClientes[1].append(Nombre)
    listaClientes[2].append(Apellido)
    listaClientes[3].append(edad)
#Verificar Contraseña
def verificarContraseña(contraseña):
    contraVeridic = True
    if len(contraseña) < 8: 
        print('Debe tener al menos 8 digitos') 
        contraVeridic = False
    if not any(char.isdigit() for char in contraseña): 
        print('La contraseña debe tener al menos 1 numero') 
        contraVeridic = False
    if not any(char.isupper() for char in contraseña): 
        print('La contraseña deberia tener al menos una Mayuscula') 
        contraVeridic = False
    if not any(char.islower() for char in contraseña): 
        print('La contraseña deberia tener al menos 1 minuscula') 
        contraVeridic = False
    if contraVeridic: 
        print('Contraseña Valida')
        listaClientes[4].append(contraseña)
#Eliminar Clientes por ID
def eliminarClientes(index):
    listaClientes[0].pop(index)
    listaClientes[1].pop(index)
    listaClientes[2].pop(index)
    listaClientes[3].pop(index)
    listaClientes[4].pop(index)
#Mostrar informacion por cliente
def mostrarInformacion(idcliente):
    id = listaClientes[0][idcliente]
    Nombre = listaClientes[1][idcliente]
    Apellido = listaClientes[2][idcliente]
    Edad = listaClientes[3][idcliente]
    Contraseña = listaClientes[4][idcliente]
    print('Id Cliente: ',id,)
    print('Nombre Cliente: ', Nombre)
    print('Apellido Cliente: ', Apellido)
    print('Edad Cliente: ', Edad)
    print('Contraseña Cliente: ', Contraseña)
#Constante
ejecutar = True
#Bucle del programa
#Bienvenida al Programa
while ejecutar:
    print('Control de Clientes')
    menuPrincipal=input("Ingrese 1, para agregar clientes \nIngrese 2, eliminar un cliente \nIngrese 3, solicitar informacion de un cliente \nIngrese su opción: ")
    if menuPrincipal == '1':
        nombreClienteN=input('Ingrese su nombre: ').title()
        apellidoClienteN=input('Ingrese su Apellido: ').title()
        edadClienteN=input('Ingrese su Edad: ')
        inputContraseña=input('Ingrese su contraseña: ')
        contraseñac = verificarContraseña(inputContraseña)
        clienteNuevo(nombreClienteN,apellidoClienteN,edadClienteN)
        continuacion1=input('¿Desea realizar otra operacion? Si/No: ').lower()
        if continuacion1 == 'si':
            continue
        elif continuacion1 == 'no':
            print('Programa terminado')
            ejecutar=False
    elif menuPrincipal =='2':
        clienteEliminado=int(input('Ingrese ID del cliente a eliminar: '))
        eliminarClientes(clienteEliminado)
        continuacion1=input('¿Desea realizar otra operacion? Si/No: ').lower()
        if continuacion1 == 'si':
            continue
        elif continuacion1 == 'no':
            print('Programa terminado')
            ejecutar=False
    elif menuPrincipal == '3':
        infoCliente=int(input('Ingrese ID del cliente que requiere informacion: '))
        mostrarInformacion(infoCliente)
        continuacion1=input('¿Desea realizar otra operacion? Si/No: ').lower()
        if continuacion1 == 'si':
            continue
        elif continuacion1 == 'no':
            print('Programa terminado')
            ejecutar=False
    else: 
        ('Ingrese una opcion valida')

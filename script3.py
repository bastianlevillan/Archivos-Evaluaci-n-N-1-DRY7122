numero_acl = input("Ingrese el numero de ACL IPv4: ")

# Determinar si el numero de ACL es Estandar, Extendida o no existe
if numero_acl.isdigit():
    numero_acl = int(numero_acl)
    if numero_acl >= 1 and numero_acl <= 99:
        print("El numero de ACL " + str(numero_acl) + " es una ACL Estandar.")
    elif numero_acl >= 100 and numero_acl <= 199:
        print("El numero de ACL " + str(numero_acl) + " es una ACL Extendida.")
    else:
        print("El numero de ACL " + str(numero_acl) + " no corresponde a una lista de acceso.")
else:
    print("El valor ingresado no es un numero de ACL valido.")
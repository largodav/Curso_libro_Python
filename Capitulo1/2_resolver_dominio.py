import socket 
dominio = input()
try:
    print("Obtener ip a partir de nombre de dominio:")
    ip=socket.gethostbyname(dominio)
    print(ip)
    print("\nObtener host a partir de direccion ip")
    print(socket.gethostbyaddr(str(ip)))
    print("Obtener nombre cualificado de un dominio")
    print(socket.getfqdn(dominio))
except socket.error as error:
    print(str(error))
    print("Error de conexion")


import socket
import sys
def comprobarListaPuertos(ip,portlist):
    try:
        for port in portlist:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result=sock.connect_ex((ip,port))
            if result == 0:
                print("Puerto {}:\t Abierto ".format(port))
            else:
                print("Puerto {}:\t Cerrado ".format(port))
            sock.close()
    except socket.error as error:
        print(str(error))
        print("Error de conexion")
comprobarListaPuertos('www.google.es',[80,8080,443,22])


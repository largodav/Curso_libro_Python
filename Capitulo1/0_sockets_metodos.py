import socket
import sys 
try:
    print("gethosbyname")
    print(socket.gethostbyname_ex('www.google.es'))
    print("\ngethostbyaddr")
    print(socket.gethostbyaddr('216.58.211.228'))
    print("\ngetfqdn")
    print(socket.getfqdn('www.yahoo.es'))
except socket.error as error:
          print (str(error))
          print('Error de conexion...')
          sys.exit()






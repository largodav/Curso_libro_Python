import socket
print('Creando socket...')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket creado')

target_host="www.google.es"
target_port= 80
print("Conexion con el host remoto")
s.connect((target_host,target_port))
print("Connection OK")

request = "GET /HTTP/1.1\r\nHost:%s\r\n\r\n" %target_host 
s.send(request.encode())

data=s.recv(4096)
print("DAtos",repr(data))
print("Longitud",len(data))
print("Cerrando el socket")
s.close()



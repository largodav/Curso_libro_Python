import socket

#crear un socket del tipo TCP y vincularlo a un puerto
#utilizamos localhost por lo tanto solo aceptamos conexiones desde la misma maquina
#el puerto podria ser el 80 pero como necesita priviligeios de root, utilizaremos el 8080

mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#permite conectar la direccion con el socket en el puerto indicado
mySocket.bind(('localhost',8080))
#poner en cola un maximo de 5 solicitudes de conexion TCP
mySocket.listen(5)

#aceptar conexiones, leer datos entrantes y responder una pagina HTML(en un bucle)
while True:
    print("Waiting for connections")
    (recvSocket,address)= mySocket.accept()
    print('HTTP request received:')
    print(recvSocket.recv(1024))
    recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n <html><body><h1>Hello world</h1></body></html>\r\n",'utf-8'))
    recvSocket.close()



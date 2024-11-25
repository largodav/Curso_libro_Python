import socket 
webhost = 'localhost'
webport = 8080
print(f"Contacting {webhost} on port {webport}")
webclient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
webclient.connect((webhost,webport))
webclient.send(bytes("GET/HTTP/1.1\r\nHost:
                     localhost\r\n\r\n".encode('utf-8')))
reply= webclient.recv(4096)
print("Response from %s:"% webhost)
print(reply.decode())



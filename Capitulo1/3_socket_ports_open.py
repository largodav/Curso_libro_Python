import socket 
ip="127.0.0.1"
portlist=[22,23,80,912,135,445,20,631]
for port in portlist:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((ip,port))
    print(port,".",result)
    sock.close()


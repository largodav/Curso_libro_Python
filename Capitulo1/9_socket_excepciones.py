import socket, sys
host = "domain/ip_address"
port=9999
host="www.bing.com"
port=111

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(5)
except socket.error as e:
    print("socket create error:%s %e")
    sys.exit()
try: 
    s.connect((host,port))
    print(s)
except socket.timeout as e:
    print("Timeout %s"%e)
    sys.exit(1)
except socket.error as e:
    print("Connection error:%s"%e)
    sys.exit(1)



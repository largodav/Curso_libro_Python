import optparse

from socket import *
from threading import *

def socketScan(host,port):
    try:
        socket_connect=socket(AF_INET,SOCK_STREAM)
        socket_connect.settimeout(10)
        socket_connect.connect((host,port))
        print('[+]%d/tcp open \n'%port)
    except Exception as error:
        print(error)
        print('[-]%d/tcp closed \n'%port)
    finally:
        socket_connect.close()

def portScanning(host,ports):
    try:
        ip=gethostbyname(host)
    except:
        print("[-]Cannot resolve '%s':Unknown host"%host)
        return
    try:
        name = gethostbyadrr
        print('\n[+]Scan results for:'+ name[0])
    except:
        print('\n[+]Scan Results for: '+ip)
    for port in ports:
        t= Thread(target=socketScan,args=(ip,int(port)))
        t.start()

def main():
        print("Entrando en main...")
        parser = optparse.OptionParser('socket_portScan'+'-H <Host> -P <Port>')
        parser.add_option('-H',dest='host',type='string',help='specify host')
        parser.add_option('-P',dest='port',type='string',help='specify port[s] separated by comma')
        (options,args)= parser.parse_args()
        host=options.host
        ports=str(options.port).split(',')
        if(host == None) | (ports[0] == None):
            print(parser.usage)
            exit(0)
        portScanning(host,ports)

if __name__=='__main__':
    #print("Entrando en main...")
    main()

import socket
import sys
ip = input("Digite o IP:")
ports = range(1, 1025)
for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.06)
    code = client.connect_ex((ip, port))
    
    if code == 0:
        print(str(port) + " - Porta aberta", )
    client.close()
print("Scan finalizada")

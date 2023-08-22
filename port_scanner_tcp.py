import socket
ip = input("Digite o IP:")
ports = range(1, 1025)
open_ports = False
print("Procurando portas...\n")
try:
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((ip, port))
        if code == 0:
            print(str(port) + " - Porta aberta", )
            open_ports = True
            client.close()


    if not open_ports:
        print("Portas abertas não encotradas")
except:
    print("Endereço de IP invalido.")
 
print("Scan finalizada")

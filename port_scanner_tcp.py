

import socket

# Solicita ao usuário para inserir o endereço IP alvo.
ip = input("Digite o IP:")

# Cria uma lista de números de porta de 0 a 1023.
ports = range(1024)

# Loop para cada número de porta na lista.
for port in ports:
    # Cria um soquete TCP e define um tempo limite de 0.05 segundos.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    
    # Tenta conectar ao IP e porta atual.
    code = client.connect_ex((ip, port))
    
    # Se a conexão tiver êxito (código 0), exibe "Porta aberta" com o número da porta.
    if code == 0:
        print(str(port) + " - Porta aberta")
print("Scan finalizada")

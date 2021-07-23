import socket 

target_host = "0.0.0.0"
target_port = 9999

#Criando um object de socket
client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

#Conectando o cliente 
client.connect ((target_host,target_port))

#Enviando alguns dados
client.send ("GET / HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n")

#Recebendo alguns dados
response = client.recv (4096)

print response
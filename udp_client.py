import socket

target_host = "127.0.0.1"
target_port = 80

#Criando um objeto de socket 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Enviando alguns dados
client.sendto("AAABBBCCC",(target_host,target_port))

#Recebendo alguns dados
data, addr = client.recvfrom(4096)

print data

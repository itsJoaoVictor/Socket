#!/usr/bin/env python
import socket,sys,threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crição de um objeto socket

HOSTIP = input("Digite o IP do servidor: ") #Obtém o IP do servidor
PORTA = int(input("Digite a porta do servidor: ")) #Obtém a porta do servidor

try:
    server.bind((HOSTIP, PORTA)) #Associa o IP e a porta ao objeto socket
    
except socket.error: 
    print("Nao foi possível conectar ao servidor")
    sys.exit() 
    
server.listen(1) #Inicia o servidor
print("Servidor iniciado")

while True:
    conn, addr = server.accept() #Aceita conexões
    print("Conexao recebida de: ", addr)
    data = conn.recv(1024) #Recebe dados
    conn.send('HTTP/1.0 200 OK\r\n\r\n<html><body><h1>Oi Cliente</h1></body></html>\r\n') #Envia dados
    threading.Thread(target= data, args=(conn, )).start() #Inicia uma thread para cada conexão
    if not data: 
        print("Conexao encerrada")
        conn.close()
        break
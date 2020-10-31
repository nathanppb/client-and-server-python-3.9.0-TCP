import socket
i=0
ip = '127.0.0.1'       #input('digite o ip de conexao: ')
port = 7000
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                # Cria o socket TCP
print("Conectando...\n")
client_socket.connect(addr)                                                      # Estabelecendo conexao previa
print("Conectado\n")
print("Endereco do servidor: ", addr, "\n")                                      # Mostra o endereco do SERVIDOR

while i < 3:
    print ("Contagem: ", i+1, "\n")
    mensagem = input("Digite um numero: ")                                      # Digitar o numero
    client_socket.send(mensagem.encode('utf-8'))                                # envia a mensagem para o socket do SERVIDOR codificada em UTF-8
    print ("\nmensagem enviada\n")                                              # Confirmacao de que a mensagem foi enviada
    Mensagem_enviar = client_socket.recv(1024)                                  # Lendo o socket do SERVIDOR e atribuindo na variavel Mensagem_enviar
    print("Mensagem recebida do servidor: ", Mensagem_enviar, "\n")             # Mostrando a mensagem modificada do SERVIDOR
    i=i+1

client_socket.close()                                                           # Fecha o socket

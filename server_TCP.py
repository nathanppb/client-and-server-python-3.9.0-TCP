import socket
import math
i=0
host = '127.0.0.1'  #input('digite o ip do servidor: ')
port = 7000
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                 # Criando o socket TCP
serv_socket.bind(addr)                                                          # Adiciona o endereco ao socket (IP E PORTA)
serv_socket.listen(1)                                                           # Escuta as solicitacoes TCP
print ('aguardando conexao\n')
novo_socket, cliente = serv_socket.accept()                                     # cria um novo socket quando aceita a solicitacao e armazena o IP do cliente
print ('conectado\n')
print("Endereco do cliente: ", cliente, "\n")                                   # Confirmacao de que foi conectado

while i < 3:
    print ("Contagem: ", i+1, "\n")
    print ("aguardando mensagem\n")
    recebe = novo_socket.recv(1024)                                              # Atribuindo a mensagem recebida do CLIENTE na variavel "recebe"
    print ("mensagem recebida: ", recebe, "\n")                                  # Printando a mensagem do CLIENTE
    Mensagem_Modificada = math.exp(float(recebe))                                # Aplicando a funcao de euler usando a variavel da mensagem do cliente (recebe), porem convertida em float
    print ("Mensagem recebida modificada: ", Mensagem_Modificada,"\n")                # Printando a mensagem modificada pelo SERVIDOR
    Mensagem_enviar = str(Mensagem_Modificada).encode('utf-8')                   # Convertendo a mensagem para o tipo string e encodificando ela
    novo_socket.send(bytes(Mensagem_enviar))                                     # Convertendo a mensagem para o tipo bytes e enviando para o CLIENTE
    i=i+1                                                                        # Acrescentando a contagem
serv_socket.close()                                                              # Fecha o socket

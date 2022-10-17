import time
import os

def mostrarOpcoes():
    print("1 - Se você quiser adicionar um item da lista")
    print("2 - Se você quiser excluir o ultimo item da lista")
    print("3 - Se você quiser saber o tamanho da lista")
    print("4 - Se você quiser exibir os itens da lista")
    print("5 - Se você quiser ver o último item da lista")
    print("6 - Se você quiser encerrar o programa")
#função para exibir o menu de opções dentro do while

verificadorDeResposta = 0 #para verificar a resposta do usuário a cada ciclo de repetição
pilha = [] #lista simulando o comportamento de uma pilha

while verificadorDeResposta != 6:
    mostrarOpcoes() #exibindo o menu de opções
    verificadorDeResposta = int(input("resposta: ")) #recebendo e convertendo a resposta do usuario para inteiro

    if verificadorDeResposta == 1:
        valorTemporario = input("Digite o valor que deseja adicionar na pilha: ") #recebendo o valor para inserir na pilha
        
        if valorTemporario.isnumeric() == True:
            valorTemporario = int(valorTemporario) #condição para transformar numero em inteiros

        pilha.append(valorTemporario) #comando principal para adicionar um item ao final da pilha
    elif verificadorDeResposta == 2:
        print("O item removido foi: ", pilha.pop()) # comando principal para remover o ultimo item da lista
    elif verificadorDeResposta == 3:
        print("O tamanho da lista é: ", len(pilha)) # comando para exibir o tamanho da pilha (números de elementos nela)
    elif verificadorDeResposta == 4:
        print("Os itens da lista são: ") # loop para exibir todos os itens presentes na pilha
        for i in pilha:
            print(i)
    elif verificadorDeResposta == 5:
        ultimoElemento = len(pilha) - 1
        print("O ultimo item da lista é: ", pilha[ultimoElemento]) # para exibir o último elemento da pilha
    else:
        verificadorDeResposta = 6
        print("programa encerrado")
    
    time.sleep(3) #para dar um tempo de visualização dos dados exibidos em cada lista antes de reiniciar o loop
    os.system('cls')
        
    
    
        

import time
import random

## MENSAGENS PERSONALIZADAS PARA UMA LISTA DE CONTATO
agenda = []
mensagens = ["Bom dia ", "vai tomar banho ", "vamos almoçar ", " lave embaixo das axilias ao tomar banho "]
continuar = "sim"
while continuar == "sim" :
    contatos = input("Digite o nome do contato... ")
    agenda.append(contatos)
    continuar = input("Gostaria de inserir um contato? sim ou não ")


cont = 0
for contatos in agenda:
    mensagem = random.choice(mensagens)
    print (mensagem,agenda[cont])
    cont +=1
    time.sleep(5)


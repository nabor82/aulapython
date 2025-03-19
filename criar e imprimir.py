with open ('teste.txt', 'w') as file:
    for linha in range(4):
        palavra = input(f"Digite a {linha+1}º palavra: ")
        file.write(palavra + "\n")


arquivo = open('texto.txt', 'r')
for linha in arquivo:
    print (linha)

vogais = ('a,e,i,o,u')
contador = 0
for vogais in linha:
    contador =+1
print(contador)
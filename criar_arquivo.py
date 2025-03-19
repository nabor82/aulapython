with open("texto.txt", "w", encoding="utf-8") as file:
    for i in range(4):
        frase = input(f"Digite a {i+1}º frase:")
        file.write(frase + "\n")
print ("Frases salvas com sucesso!!")
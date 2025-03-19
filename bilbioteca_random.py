import random

def sorteio_aluno():
    alunos = ["José", "Ana", "pedro", "Julia", "Maria", "Fabiana"]
    escolher = random.choice(alunos)
    print (f"O aluno escolhido foi: {escolher}")

sorteio_aluno()
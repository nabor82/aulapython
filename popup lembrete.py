import tkinter as tk
import pyautogui
import time


# CRIANDO A JANELA PRINCIPAL
janela = tk.Tk()
janela.title ("Lembrar nunca é demais!")
janela.minsize(300,100)


# FUNÇÃO AO APERTAR O BOTÃO
def mostrar_mensagem():
    pyautogui.press('win')
    time.sleep (2)
    pyautogui.typewrite('word')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.typewrite('BEBA AGUA E FELIZ ANIVERSARI MANU !!!')


# CRIANDO DO BOTÃO
botao = tk.Button(janela, text = 'Clque para lembrar', command=mostrar_mensagem)
botao.pack()


janela
janela.mainloop()
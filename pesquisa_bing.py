import pyautogui
import time
import random
import string
import subprocess

# Função para gerar uma palavra aleatória
def gerar_palavra_aleatoria(tamanho):
    letras = string.ascii_lowercase
    return ''.join(random.choice(letras) for _ in range(tamanho))

# Função para gerar uma lista de palavras únicas
def gerar_lista_palavras_unicas(quantidade, tamanho_palavra):
    palavras = set()
    while len(palavras) < quantidade:
        nova_palavra = gerar_palavra_aleatoria(tamanho_palavra)
        palavras.add(nova_palavra)
    return list(palavras)

# Abre o navegador Edge usando subprocess
subprocess.Popen(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])

# Espera o navegador abrir
time.sleep(5)

# Gera uma lista de 30 palavras aleatórias com tamanho entre 5 e 10 caracteres
palavras_aleatorias = gerar_lista_palavras_unicas(30, random.randint(5, 10))

# Realiza as pesquisas
for termo_pesquisa in palavras_aleatorias:
    # Digita o termo de pesquisa e pressiona Enter
    pyautogui.write(termo_pesquisa)
    pyautogui.press('enter')
    
    # Espera os resultados
    time.sleep(13)

# Fecha a aba do navegador
pyautogui.hotkey('ctrl', 'w')
# Fecha o navegador
# pyautogui.hotkey('alt', 'f4')

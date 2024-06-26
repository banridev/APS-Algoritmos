import requests
import random

url = "https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt"
response = requests.get(url)
palavras = response.text.split('\n')

def escolher_palavra(palavras):
    palavra = random.choice(palavras)
    palavras.remove(palavra)
    return palavra

def exibir_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def desenhar_forca(tentativas):
    partes_corpo = [
        " O\n",
        "/",
        "|",
        "\\\n",
        "/ \\\n"
    ]

    if tentativas <= 4:
        print(partes_corpo[0], end='')
    if tentativas <= 3:
        print(partes_corpo[1], end='')
    if tentativas <= 2:
        print(partes_corpo[2], end='')
    if tentativas <= 1:
        print(partes_corpo[3], end='')
    if tentativas <= 0:
        print(partes_corpo[4], end='')

def fornecer_dica(palavra, letras_corretas, dicas_usadas):
    letras_nao_descobertas = [letra for letra in palavra if letra not in letras_corretas]
    letra_dica = random.choice(letras_nao_descobertas)
    dicas_usadas.append(letra_dica)
    return letra_dica

def jogo_da_forca():
    palavra = escolher_palavra(palavras)
    letras_corretas = set()
    tentativas = 5
    dicas_usadas = []

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra:")

    while tentativas > 0:
        exibir_palavra(palavra, letras_corretas)
        letra = input("Digite uma letra (ou 'dica' para dica): ").lower()

        if letra == 'dica':
            if len(dicas_usadas) < 2:
                dica = fornecer_dica(palavra, letras_corretas, dicas_usadas)
                print("Dica:", dica)
            else:
                print("Você já usou todas as dicas disponíveis.")
            continue

        if letra in letras_corretas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        if letra in palavra:
            print("Letra correta!")
            letras_corretas.add(letra)
            if len(letras_corretas) == len(set(palavra)):
                print("Parabéns! Você acertou a palavra:", palavra)
                break
        else:
            print("Letra errada!")
            tentativas -= 1
            desenhar_forca(tentativas)

    if tentativas == 0:
        print("Você perdeu! A palavra correta era:", palavra)

if __name__ == "__main__":
    jogo_da_forca()

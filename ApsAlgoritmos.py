import requests
import random

# Baixar o arquivo de palavras
url = "https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt"
response = requests.get(url)
palavras = response.text.split('\n')

# Função para escolher uma palavra aleatória
def escolher_palavra(palavras):
    palavra = random.choice(palavras)
    palavras.remove(palavra)  # Remover a palavra escolhida para evitar repetição
    return palavra

# Função para exibir a palavra atualizada com as letras corretas e espaços para letras não descobertas
def exibir_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

# Função para desenhar o boneco da forca
def desenhar_forca(tentativas):
    partes_corpo = [
        " O\n",
        "/|\\\n",
        "/ \\\n"
    ]

    for parte in partes_corpo[:tentativas]:
        print(parte, end='')

# Função principal do jogo
def jogo_da_forca():
    palavra = escolher_palavra(palavras)
    letras_corretas = set()
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra:")

    while tentativas > 0:
        exibir_palavra(palavra, letras_corretas)
        letra = input("Digite uma letra: ").lower()

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

# Chamada da função principal
if __name__ == "__main__":
    jogo_da_forca()

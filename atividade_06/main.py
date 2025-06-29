import re

def main():
    texto = input("Digite o texto a ser revisado: ")
    palavra_antiga = input("Qual palavra deseja substituir? ")
    palavra_nova = input("Qual a nova palavra? ")

    texto_revisado = re.sub(palavra_antiga, palavra_nova, texto)
    print(texto_revisado)

if __name__ == "__main__":
    main()
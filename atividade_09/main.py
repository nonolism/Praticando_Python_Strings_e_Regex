import re

def main():
    livro = input("Digite o título do livro: ")
    letra = input("Digite a letra inicial para pesquisa: ") 
    regex = re.compile(rf"\b{letra}[a-zA-Z]+", re.IGNORECASE)
    
    palavras_encontradas = re.findall(regex, livro)
    print(palavras_encontradas)

if __name__ == "__main__":
    main()
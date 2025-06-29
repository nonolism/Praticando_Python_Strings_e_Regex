import re

def main():
    padrao_receita = re.compile(r"\d+")
    descricao = input("Digite a descrição da receita: ")
    numero_receita = re.search(padrao_receita, descricao)
    
    if numero_receita:
        print(f"O número da receita é: {numero_receita.group()}")
    else:
        print("Nenhum número de receita encontrado na descrição.")
        
if __name__ == "__main__":
    main()
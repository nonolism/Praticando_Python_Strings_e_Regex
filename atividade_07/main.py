import re

def main():
    padrao_nome = re.compile(r"[A-Z][a-z]+")
    nome = input("Digite o nome do cliente para validação: ").strip()
    
    if re.fullmatch(padrao_nome, nome):
        print("Nome válido.")
    else:
        print("Nome inválido. O nome deve começar com letra maiúscula e conter apenas letras.")

if __name__ == "__main__":
    main()
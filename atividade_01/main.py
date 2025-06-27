
def padronizar_nome(nome) -> str:
    return nome.strip().lower()

def main():
    nome_produto = padronizar_nome(input("Digite o nome do produto: "))
    print(nome_produto)

if __name__ == "__main__":
    main()
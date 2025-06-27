def padronizar_texto(texto: str) -> str:
    return texto.strip().capitalize()

def main():
    nome_cliente = padronizar_texto(input("Digite o nome do cliente: "))
    cidade_cliente = padronizar_texto(input("Digite a cidade do cliente: "))
    
    print(f"Olá, {nome_cliente}! Bem-vindo(a) ao sistema da cidade de {cidade_cliente}.")

if __name__ == "__main__":
    main()
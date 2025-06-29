def main():
    inicio_obrigatorio = "https://"
    fim_obrigatorio = ".com"
    url = input("Digite a URL para validação: ")
    
    if url.startswith(inicio_obrigatorio) and url.endswith(fim_obrigatorio):
        print("URL válida")
    else:
        print("URL inválida")
    
    pass

if __name__ == "__main__":
    main()
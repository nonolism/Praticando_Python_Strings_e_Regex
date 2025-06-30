import re

def main():
    padrao_cpf = re.compile(r"\d{3}.\d{3}.\d{3}-\d{2}")
    cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")
    
    if re.fullmatch(padrao_cpf, cpf):
        print("O CPF está no formato correto.")
    else:
        print("O CPF está no formato incorreto. Deve ser no formato XXX.XXX.XXX-XX, onde X é um dígito.")

if __name__ == "__main__":
    main()
    
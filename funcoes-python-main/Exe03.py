def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

if __name__ == "__main__":
    print(par_ou_impar(5))
    print(par_ou_impar(8))

    num = int(input("Digite: "))
    print(par_ou_impar(num))
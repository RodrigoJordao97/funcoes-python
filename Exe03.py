def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "impar"

if __name__ == "__main__":
#par_ou_impar(5)
#par_ou_impar(8)

    num = int(input("Digite:"))
    par_ou_impar(num)
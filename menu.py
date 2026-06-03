import Exe01 as saudacao
import Exe02 as soma
import Exe03 as parouimpar
import Exe04 as maior
import Exe05 as calculadora
import Exe06 as vogais
import Exe07 as fatorial

saudacao.saudacao("Andressa")

print(f"A soma dos dois é: {soma.somar(10, 8)}")

print(f"O numero a seguir é: {parouimpar.par_ou_impar(17)}")

print(f"O número maior é: {maior.maior_numero(20, 10)} ")

print(f"A operação a seguir têm o resultado: {calculadora.calculadora(20, 10, '*')}")

print(f"Esta frase têm {vogais.contar_vogais(' Eu gosto de hambúrguer')} vogais")

print(f"O fatorial deste número é: {fatorial.fatorial(5)}")
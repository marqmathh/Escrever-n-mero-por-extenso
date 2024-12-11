from num2words import num2words

def numero_escrito(numero):
    return num2words(numero, lang='pt')

numero = int(input("Digite um número: "))

print(numero_escrito(numero))

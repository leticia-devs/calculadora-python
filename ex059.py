from operator import truediv

prim =int(input("Digite o valor do primeiro número: "))
seg = int(input("Digite o valor do segundo número: "))
valor = 0

while valor != 5:
    valor = int(input("""
=-=-=-=-=-=-=-=-=-=-=
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do progama
=-=-=-=-=-=-==-=-=-=-=
Digite o valor: """))

    if valor == 1:
        valor = (prim + seg)
        print("A soma de {} com {} é {}!!!".format (prim, seg, valor))
    elif valor == 2:
        valor = (prim * seg)
        print("A multiplicação de {} com {} é igual a {}!!!".format(prim, seg, valor))
    elif valor == 3:
        if prim > seg:
            print("O número maior é {}".format(prim))
        else:
            print("O número maior é o {}".format(seg))
    elif valor == 4:
        prim = int(input("Digite o valor do primeiro número: "))
        seg = int(input("Digite o valor do segundo número: "))

print ("Fim do progama!!!!!!!")3
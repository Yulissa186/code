a = int (input("ingresa el primer numero "))
b = int (input("ingresa otro numero "))
print ("{+} suma a+b")
print("{-} resta a-b")
print("{*} multiplica a*b")
print("{/} divide a/b")
simbolo = input("ingresa la operacion insertando el simbolo")
match simbolo:
    case "+":
        print("el resultado", (a+b))
    case "-":
        print("el resautado ", (a-b))
    case "*":
        print("el resultado", (a*b))
    case "/":
        if b !=0:
            print("el resultado", (a/b))
        else:
            print("no se puede dividir entre cero")
    case _:
        print("operacion invalida")

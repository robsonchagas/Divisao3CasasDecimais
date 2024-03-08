valor1 = input("Insera o primeiro valor: ")
entrada1 = float(valor1.replace("," , "."))
valor2 = input("Insera o segundo valor: ")
entrada2 = float(valor2.replace("," , "."))
divisao = entrada1 / entrada2
divisaoFormatada = "{:.3f}".format(divisao)
print(divisaoFormatada)
import time
while True:
    print("calculadora 2 digitos - DIGITE - S / N - para iniciar")
    start = (input("Iniciar? "))
    
    if start == "S" or start == "s":
        while True:
            print("Calculadora de 2 digitos\n")
            print("Atenção as instruções!\n")
            print("Digite + para somar\n")
            print("Digite - para subtrair\n")
            print("Digite * para multiplicar\n")
            print("Digite / para dividir\n")
            print("Digite ** para exponenciação\n")
            print("Digite % para módulo\n")
            entrada = input(": ")
            if entrada in ["+"]:
                print("SOMAR")
                num1 = float(input("Digite um número: "))
                num2 = float(input("Digite um segundo número: "))
                print("Calculando... \n\n\n\n")
                print(f"A soma de {num1} + {num2} é {num1 + num2} ")
                time.sleep(1)
                SouN = input("De novo? (S/N): ")
                if SouN == "S" or SouN == "s":
                    print("...")
                    time.sleep(1)
                else:
                    exit()
                    
            elif entrada in ["-"]: 
                print("SUBTRAIR")
                num1 = float(input("Digite um número: "))
                num2 = float(input("Digite um segundo número: "))
                print("Calculando... \n\n\n\n")
                print(f"A subtração de {num1} - {num2} é {num1 - num2} ")
                time.sleep(1)
                SouN = input("De novo? (S/N): ")
                if SouN == "S" or SouN == "s":
                    print("...")
                    time.sleep(1)
                else:
                    exit()

            elif entrada in ["*"]:
                print("MULTIPLICAR")
                num1 = float(input("Digite um número: "))
                num2 = float(input("Digite um segundo número: "))
                print("Calculando... \n\n\n\n")
                print(f"A multiplicação de {num1} vezes {num2} é {num1 * num2} ")
                time.sleep(1)
                SouN = input("De novo? (S/N): ")
                if SouN == "S" or SouN == "s":
                    print("...")
                    time.sleep(1)
                else:
                    exit()

            elif entrada in ["/"]:
                print("DIVIDIR")
                num1 = float(input("Digite um número: "))
                num2 = float(input("Digite um segundo número: "))
                print("Calculando... \n\n\n\n")
                print(f"{num1} dividido por {num2} é {num1 / num2} ")
                time.sleep(1)
                SouN = input("De novo? (S/N): ")
                if SouN == "S" or SouN == "s":
                    print("...")
                    time.sleep(1)
                else:
                    exit()
            elif entrada in ["**"]:
                print("EXPONENCIAÇÃO")
                num1 = float(input("Digite um número: "))
                num2 = float(input("Digite um segundo número: "))
                print("Calculando... \n\n\n\n")
                print(f"A exponenciação de {num1} elevado a {num2} é {num1 ** num2} ")
                time.sleep(1)
                SouN = input("De novo? (S/N): ")
                if SouN == "S" or SouN == "s":
                    print("...")
                    time.sleep(1)
                else:
                    exit()

            elif entrada in ["%"]:
                print("RESTO DE DIVISÃO")
                num1 = float(input("Digite um número: "))
                num2 = float(input("Digite um segundo número: "))
                print("Calculando... \n\n\n\n")
                print(f"O resto da divisão {num1} dividido por {num2} é {num1 % num2} ")
                time.sleep(1)
                SouN = input("De novo? (S/N): ")
                if SouN == "S" or SouN == "s":
                    print("...")
                    time.sleep(1)
                else:
                    exit()
            else:
                print("esta invalido")
                break
                
    elif start == "N" or start == "n":
        print("Tchau!!!")
        exit()
    else:
        print("desculpe, digite novamente?")
#POR Miguel Camilo! OBRIGADO!
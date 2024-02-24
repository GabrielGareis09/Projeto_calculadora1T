def calculadora():
    while True:
        print("\nSelecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite o número da operação desejada: ")

        if escolha == '5':
            print("Calculadora encerrada.")
            break

        if escolha in ('1', '2', '3', '4'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = num1 + num2
                print(f"A soma é: {resultado}")
            elif escolha == '2':
                resultado = num1 - num2
                print(f"A subtração é: {resultado}")
            elif escolha == '3':
                resultado = num1 * num2
                print(f"A multiplicação é: {resultado}")
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"A divisão é: {resultado}")
                else:
                    print("Não é possível dividir por zero.")
        else:
            print("Escolha inválida. Tente novamente.")

# Chame a função para iniciar a calculadora
calculadora()

</body>
</html>

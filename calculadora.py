# Calculadora Python Interativa
# Projeto educacional - Operações matemáticas básicas

def adicao(a, b):
    """Soma dois números"""
    return a + b

def subtracao(a, b):
    """Subtrai o segundo número do primeiro"""
    return a - b

def multiplicacao(a, b):
    """Multiplica dois números"""
    return a * b

def divisao(a, b):
    """Divide o primeiro número pelo segundo"""
    if b == 0:
        return "Erro: Divisão por zero não é permitida!"
    return a / b

def potencia(a, b):
    """Eleva o primeiro número à potência do segundo"""
    return a ** b

def menu():
    """Exibe o menu de operações"""
    print("\n" + "="*50)
    print("🧮 CALCULADORA PYTHON")
    print("="*50)
    print("\nEscolha uma operação:")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (×)")
    print("4. Divisão (÷)")
    print("5. Potência (^)")
    print("0. Sair")
    print("="*50)

def executar_calculadora():
    """Função principal que executa a calculadora"""
    while True:
        menu()
        
        try:
            opcao = int(input("\nDigite o número da operação: "))
            
            if opcao == 0:
                print("\n👋 Obrigado por usar a Calculadora Python!")
                print("Desenvolvido por Vinicius Alves Silva")
                break
            
            if opcao not in [1, 2, 3, 4, 5]:
                print("\n❌ Opção inválida! Escolha entre 0 e 5.")
                continue
            
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if opcao == 1:
                resultado = adicao(num1, num2)
                operador = "+"
            elif opcao == 2:
                resultado = subtracao(num1, num2)
                operador = "-"
            elif opcao == 3:
                resultado = multiplicacao(num1, num2)
                operador = "×"
            elif opcao == 4:
                resultado = divisao(num1, num2)
                operador = "÷"
            elif opcao == 5:
                resultado = potencia(num1, num2)
                operador = "^"
            
            print(f"\n✅ Resultado: {num1} {operador} {num2} = {resultado}")
            
            input("\nPressione ENTER para continuar...")
            
        except ValueError:
            print("\n❌ Erro: Digite apenas números válidos!")
            input("\nPressione ENTER para continuar...")
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            input("\nPressione ENTER para continuar...")

# Executar o programa
if __name__ == "__main__":
    executar_calculadora()


#algoritmo02

def fibonacci_sequencia(limit):
    sequencia = [0, 1]
    while True:
        novo_valor = sequencia[-1] + sequencia[-2]
        if novo_valor > limit:
            break
        sequencia.append(novo_valor)
    return sequencia

def check_fibonacci_number(num):
    fib_sequencia = fibonacci_sequencia(num)
    if num in fib_sequencia:
        return True, fib_sequencia
    return False, fib_sequencia

if __name__ == "__main__":
    num_to_check = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    
    pertence, sequencia = check_fibonacci_number(num_to_check)
    
    if pertence:
        print(f"O número {num_to_check} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num_to_check} NÃO pertence à sequência de Fibonacci.")
    
    print("Sequência de Fibonacci gerada:", sequencia)

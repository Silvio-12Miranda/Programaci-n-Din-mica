def fibonacci_recursivo(n):
        if n == 0 or n == 1:
            return 1
        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def run():
    n = int(input('Escribe un numero: '))
    resultado = fibonacci_recursivo(n)
    print(resultado)

if __name__ == '__main__':
    run()

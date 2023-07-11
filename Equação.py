import math

def solve_quadratic_equation(a, b, c):
    delta = b**2 - 4*a*c
    
    if delta < 0:
        # Não há soluções reais
        return None
    elif delta == 0:
        # Há uma solução real
        x = -b / (2*a)
        return x
    else:
        # Há duas soluções reais
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

# Teste para equação 
a = 4
b = -9
c = 2

solutions = solve_quadratic_equation(a, b, c)
if solutions is None:
    print("A equação não possui soluções reais.")
elif isinstance(solutions, tuple):
    x1, x2 = solutions
    print(f"As soluções da equação são: x1 = {x1} e x2 = {x2}.")
else:
    x = solutions
    print(f"A única solução da equação é: x = {x}.")

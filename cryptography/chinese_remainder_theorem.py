from sympy.ntheory.modular import crt

# n mod(3) = 2
# n mod(5) = 3
# n mod(7) = 2
N = [3, 5, 7]  # Modulus
R = [2, 3, 2]  # Results

if __name__ == '__main__':
    crt_result = crt(N, R)[0]
    print(f'Result of the Chinese Remainder Theorem = {crt_result}')

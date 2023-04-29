from sympy.ntheory.modular import crt

# n mod(3) = 2
# n mod(5) = 3
# n mod(7) = 2
MODULUS = [3, 5, 7]
RESULTS = [2, 3, 2]

if __name__ == '__main__':
    crt_result = crt(MODULUS, RESULTS)[0]
    print(f'Result of the Chinese Remainder Theorem = {crt_result}')  # crt_result = 23

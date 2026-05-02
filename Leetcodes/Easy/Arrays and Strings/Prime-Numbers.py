def prime_numbers(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 55]

if __name__ == "__main__":
    for number in Numbers:
        print(number, prime_numbers(number))
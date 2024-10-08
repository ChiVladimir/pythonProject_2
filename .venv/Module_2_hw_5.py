numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_prime = list()

for i in range(0, len(numbers)):
    n = numbers[i]
    if n > 1:
        for i in range(2, (n // 2) + 1):
            if (n % i) == 0:
#                print(n, "is not a prime number")
                not_prime.append(n)
                break
        else:
#            print(n, "is a prime number")
            primes.append(n)


print('Primes: ', primes)
print('Not primes:', not_prime)
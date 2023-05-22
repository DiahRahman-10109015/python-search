def sequential_search_prime(data):
    primes = []
    for num in data:
        if num > 1: 
            is_prime = True
            for i in range(2, num):
                if (num % i) == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

# Daftar bilangan
numbers = [7, 10, 13, 6, 17, 22, 19]

# Mencari bilangan prima dari daftar bilangan
prime_numbers = sequential_search_prime(numbers)

#Menampilkan bilangan prima
print("Bilangan prima dalam daftar tersebut yaitu:",prime_numbers)   
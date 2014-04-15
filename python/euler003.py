
largest_prime_factor = 1
number = 600851475143

while number > 1:
    largest_prime_factor += 1
    while number % largest_prime_factor == 0:
        number /= largest_prime_factor
    
print largest_prime_factor

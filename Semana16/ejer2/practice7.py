def isPrimeNumber(my_number):
    count = 0
    if my_number > 1:
        for i in range(1,my_number + 1 ):
            if my_number % i == 0:
                count += 1
                if count > 2:
                    return False
        return True
    else:
        return False

    
def primeNumbers(my_list):
    new_list = []
    for element in my_list:
        if isPrimeNumber(element):
            new_list.append(element)
    return new_list


my_numbers = [1, 4, 6, 7, 13, 9, 67] 
my_primes = primeNumbers(my_numbers)
if len(my_primes) > 0:
    print(f"The prime numbers from {my_numbers} are {my_primes}")
else:
    print(f"No prime numbers were found in {my_numbers}")
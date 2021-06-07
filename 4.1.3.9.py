def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            print(num,"is not a prime no.")
            return False
        else:
            print(num, 'is a prime no.')
            return True

is_prime(31)

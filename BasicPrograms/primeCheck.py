def prime(n):
    if n > 1:
        for i in range(2, int(n//2)+1):
            if n % i == 0:
                print('This is not a prime number.')
                break
        else:
            print('This is a prime number.')
    else:
        print('This is not a prime number.')

prime(23)

fizz = 'Fizz'
buzz = 'Buzz'

def fizzbuzz(num):
    if num % 15 == 0:
        return fizz + buzz
    if num % 3 == 0:
        return fizz
    elif num % 5 == 0:
        return buzz
    else:
        return str(num)

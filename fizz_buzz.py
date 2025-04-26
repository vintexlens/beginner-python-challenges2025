while True:
    def fizz_buzz(number):
        if number % 3 == 0 and number % 5 == 0:
            return 'FizzBuzz'
        if number % 3 == 0:
            return 'Fizz'
        if number % 5 == 0:
            return 'Buzz'
        return number
    number=int(input("Enter number"))
    print(fizz_buzz(number))

    tryagain=input("Do you want to try again?yes/no").lower()
    if tryagain.startswith('n'):
        print('Goodbye')
        break

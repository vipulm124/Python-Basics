def check_prime(num):
    listRange = list(range(1,num + 1))
    divisorList = []
    for number in listRange:
        if num % number == 0:
            divisorList.append(number)
            return
        if len(divisorList) == 2:
            print("It's a prime number")


number = input("Please enter a number.")

number = int(number)
check_prime(number)
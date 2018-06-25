

def check_prime(num):
    listRange = list(range(1,num + 1))
    divisorList = []
    for n in listRange:
        if(num%n==0):
            divisorList.append(n)
    if len(divisorList)==2:
        print(" is a prime number")
    else:
        print(" is not a prime number")
        return

number = input("Please enter a number.")
number = int(number)
check_prime(number)
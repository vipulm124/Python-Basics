number = input("Please enter a number ")
number = int(number)

mod = number % 2
if mod > 0:
    print("You entered an odd number")
else:
    print("You entered an even number")



def generateFibonacci(count):
    fib=[]
    for index in range(0,count):
        if(index==0):
            fib.append(1)
        elif(index==1):
            fib.append(1)
        else:
            fib.append(int(fib[index-2])+int(fib[index-1]))
    print(fib)
    return


input = int(input("Please enter count "))
generateFibonacci(input)

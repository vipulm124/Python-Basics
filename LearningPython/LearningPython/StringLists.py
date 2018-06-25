string = input("Enter a string ")

#Method 1
reverse = ''
for i in range(len(string)):
    reverse += string[len(string)-1-i]

if reverse==string:
    print("String is a pallindrome. ")
else:
    print("Not a pallindrome. ")

#Method 2
rvs = string[::-1]
if rvs == string:
        print("String is a pallindrome. ")
else:
    print("Not a pallindrome. ")

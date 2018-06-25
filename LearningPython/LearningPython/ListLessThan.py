a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Choose a number: "))

new_List=[]

for i in a:
    if i<num:
        new_List.append(i)

print(new_List)


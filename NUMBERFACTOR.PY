def func(a):
    b=[]
    for i in a:
        if  i not in b:
            b.append(i)
    b.sort()
    return b
a=eval(input("Enter list:"))
print("The list after removing duplicates is:",func(a))


OUTPUT : 
Enter list:23,43,12,32,34,23,22
The list after removing duplicates is: [12, 22, 23, 32, 34, 43]

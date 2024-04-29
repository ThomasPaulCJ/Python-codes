n=int(input("How many numbers"))

nums=[]

for i in range(n):
    nums.append(int(input("Enter number")))
nums.sort()
print("sorted list is",nums)
nums.reverse()

print("reverse list is",nums)
x=int(input("enter number to be searched for : "))
print("The number is found at index",nums.index(x))
y=int(input("Enter number to find its count : "))
print("The number is found",nums.count(y),"times")
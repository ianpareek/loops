n = int(input("Enter the number whose sum you want to find: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
    print("The sum of whole numbers is:", sum)


a = int(input("Enter the range of numbers you want to be printed: ")) 
for i in range(1, a + 1):
    if i % 2 != 0:
        print(i)
num = int(input('Enter number to check the prime status: '))

for i in range(2, num):
    if (num % i) == 0:
        print(num, 'is Not Prime Number.')
        break
else:
    print(num, 'is a Prime Number.')
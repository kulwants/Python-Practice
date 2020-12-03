a = [[17,29], [32,41]]
new_list = [x for b in a for x in b]                # Nested List
print('Nested List: ' + str(new_list))

odds = [x for x in range(10) if x%2 == 1]           # Odd Numbers
print('Odd Numbers: ' + str(odds))

ten_x = [x * 10 for x in range(10)]                 # Multiples of 10
print("Multiles of 10: " + str(ten_x))

under_10 = [x for x in range(10)]                   # Values within Range
print("Values witin Range: " + str(under_10))

square = [x ** 2 for x in under_10]                 # Squares
print('Squares: ' + str(square))

k = 'Kulwant Singh Saggu'
c = 'Start : End : Step'
print(k + "  ||  " + c + "  ||  " + k[3::2])


count = 0
while (count < 3):      
    count = count + 1
    print("KS")  
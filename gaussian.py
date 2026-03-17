matrix = [[2, 4, -2, 2], [4, 9, -3, 8], [-2, -3, 7, 10]]
print(matrix[1])

m = matrix[1][0] / matrix[0][0]

print(m)
new_list = []
for i in matrix[0]:
    ma = i * m
    print(ma)
    
    new_list.append(ma)
print(new_list)
                            
print(ma)

new_row2 = []

for index, value in enumerate(matrix[1]):
    for index2, value2 in enumerate(new_list):
        if index == index2:
            row2 = value - value2
            new_row2.append(row2)

print(new_row2)
            
matrix[1] = new_row2

print(matrix)

#THIS IS FOR ROW3 COLUMN 1 

print("------------------------------")
m2 = matrix[2][0] / matrix[0][0]
print(m2)


new_list2 = []

for i in matrix[0]:
    multiply = i * m2
    print(multiply)
    new_list2.append(multiply)
    print(new_list2)

new_row3 = []
for index, value in enumerate(matrix[2]):
    for index2, value2 in enumerate(new_list2):
        if index == index2:
            row3 = value - value2
            new_row3.append(row3)
print(new_row3)

matrix[2] = new_row3

print(matrix)

#THIS IS FOR ROW3 COLUMN 2

print("------------------------------")

m3 = matrix[2][1] / matrix[1][1]

print(f" here is Multipler for Row 3 col 2: {m3}")

new_list3 = []

for i in matrix[1]:
    multipler = i * m2
    print(multipler)
    new_list3.append(multipler)
    print(new_list3)
    
    
new_row4 = []
for index, value in enumerate(matrix[2]):
    for index2, value2 in enumerate(new_list3):
        if index == index2:
            row4 = value2 + value
            new_row4.append(row4)
print(f'Here is Row 3 Col2: {new_row4}')

matrix[2] = new_row4

print(matrix)


#BACK SUBSTITUTION
print("")
print("BACK SUBSTITION----------------------->")

z = matrix[2][3] / matrix[2][2]
print(z)

y =  matrix[1][3] / z
print(y)
'''
cal = (4 * 2) - (2 * 2)
print(cal)
'''
y_value =  matrix[1][3] * y 
z_value =  matrix[2][3] * z
x = matrix[0][3] - y_value - z_value / matrix[0][3]
print(x)

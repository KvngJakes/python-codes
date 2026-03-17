matrix = [[1, 1, 1, 6], [2, -1, 1, 3], [-1, 2, 3, 12]]

def row2():
    # STEP 1: Eliminate first column from rows 2 and 3
    print("STEP 1: Eliminating first column")
    for x in range(1, 3):
        m1 = matrix[x][0] / matrix[0][0]
        print(f"Multiplier for row {x+1}: {m1}")
        
        new_list = []
        for i in matrix[0]:
            new_list.append(i * m1)
        
        new_row = []
        for index, value in enumerate(matrix[x]):
            new_row.append(value - new_list[index])
        
        matrix[x] = new_row
        print(f"Row {x+1} becomes: {matrix[x]}")
    
    print("\nMatrix after step 1:")
    for row in matrix:
        print(row)
    
    # STEP 2: Eliminate second column from row 3
    print("\nSTEP 2: Eliminating second column from row 3")
    m2 = matrix[2][1] / matrix[1][1]
    print(f"Multiplier: {m2}")
    
    new_list = []
    for i in matrix[1]:
        new_list.append(i * m2)
    
    new_row = []
    for index, value in enumerate(matrix[2]):
        new_row.append(value - new_list[index])
    
    matrix[2] = new_row
    
    print("\nFinal matrix:")
    for row in matrix:
        print(row)

row2()

# BACK SUBSTITUTION
print("\nBACK SUBSTITUTION ----------------------------------------->")
z = matrix[2][3] / matrix[2][2]
print(f"z = {z}")

y = (matrix[1][3] - matrix[1][2] * z) / matrix[1][1]
print(f"y = {y}")

x = (matrix[0][3] - matrix[0][1] * y - matrix[0][2] * z) / matrix[0][0]
print(f"x = {x}")

print(f"\nSolutions: x = {x}, y = {y}, z = {z}")
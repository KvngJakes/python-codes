matrix = [[1, 1, 1, 6], [2, -1, 1, 3], [-1, 2, 3, 12]]

def forward_elimination():
    # For each pivot row
    for pivot_row in range(len(matrix)-1):
        pivot_element = matrix[pivot_row][pivot_row]
        
        # Eliminate rows below the pivot row
        for row in range(pivot_row + 1, len(matrix)):
            # Calculate multiplier using pivot row, not the current row
            multiplier = matrix[row][pivot_row] / pivot_element
            
            print(f'Multiplier for row {row} using pivot row {pivot_row}: {multiplier}')
            
            # Create the new row by subtracting multiplier * pivot row
            new_row = []
            for col in range(len(matrix[row])):
                new_value = matrix[row][col] - multiplier * matrix[pivot_row][col]
                new_row.append(new_value)
            
            # Replace the row
            matrix[row] = new_row
            
            print(f'Updated row {row}: {matrix[row]}')

print("Original matrix:")
for row in matrix:
    print(row)

print("\nPerforming Gaussian elimination:")
forward_elimination()

print("\nMatrix after forward elimination:")
for row in matrix:
    print(row)

# Now you can do back substitution to find the solutions
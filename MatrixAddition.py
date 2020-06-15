''' Question: Write a Python program to add 2 matrices.

Solution: '''

def add_matrices(matrix1, matrix2):
    result = []
    
    #iterating over the rows
    for i in range(len(matrix1)):
        output_rows = []
        #iterating over the columns
        for j in range(len(matrix1[0])):
            output_rows.append(matrix1[i][j] + matrix2[i][j])
        result.append(output_rows)
        
    return result

#entry point of the program
if __name__ == '__main__':
    rows = int(input('Enter number of rows: '))
    columns = int(input('Enter number of columns: '))
    
    #initializing matrix1
    matrix1 = []
    print("Enter the matrix1 elements row-wise...")
    
    for i in range(rows):
        a = []
        for j in range(columns):
            a.append(int(input()))
        matrix1.append(a)
        
    #initializing matrix2
    matrix2 = []
    print("Enter the matrix2 elements row-wise...")
    
    for i in range(rows):
        b = []
        for j in range(columns):
            b.append(int(input()))
        matrix2.append(b)
        
    sum_matrix = add_matrices(matrix1, matrix2)
    
    #displaying the output matrix
    print("Output Matrix is:- ")
    for i in range(rows):
        for j in range(columns):
            print(sum_matrix[i][j], end = " ")
        print()

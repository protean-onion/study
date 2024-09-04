#! /usr/bin/python3

from random import randint

def create_random_array(rows, columns):
    return [[randint(0, 100) for column in range(columns)] for row in range(rows)]
        
def columns(matrix):
    column_matrix = []
    for column_index in range(len(matrix[0])):
        column = []
        for row in matrix:
            column.append(row[column_index])
        column_matrix.append(column)
    return column_matrix

def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrices don't align.")
        
    matrix2_columns = columns(matrix2)
    
    product_matrix = []
    for row in matrix1:
        product_row = []
        for column in matrix2_columns:
            product_row_element = 0
            for rank in range(len(matrix1[0])):
                product_row_element = row[rank] * column[rank]
            product_row.append(product_row_element)
        product_matrix.append(product_row)
    return product_matrix

def take_input():
    rows, columns = [int(element.strip(" ")) for element in input("Input matrix dimensions in the format `rows columns`.\n-> ").split(" ")]
    return rows, columns

def main():
   while True:
        try:
            print("Matrix 1")
            rows, columns = take_input()
            matrix1 = create_random_array(rows, columns)
            for row in matrix1:
                print(row)
            print("")

            print("Matrix 2")
            rows, columns = take_input()
            matrix2 = create_random_array(rows, columns)
            for row in matrix2:
                print(row)
            print("")

            product_matrix = matrix_multiplication(matrix1, matrix2)
            print("Product Matrix")
            for row in product_matrix:
                print(row)      
            print("")
        except ValueError:
            print("Either input format is not appropriate or dimensions do not match.\nTry again.\n")

if __name__ == "__main__":
    main()

import numpy as np
def create_magic_square():
    magic_square = np.array([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
    return magic_square

def verify_magic_square(magic_square):
    row_sums = np.sum(magic_square, axis = 1)
    col_sums = np.sum(magic_square, axis = 0)
    diag_sums = [np.sum(np.diag(magic_square)), np.sum(np.diag(np.fliplr(magic_square)))]

    all_equal = (
        np.all(row_sums == row_sums[0]) and
        np.all(col_sums == col_sums[0]) and
        diag_sums[0] == diag_sums[1] == row_sums[0]
    )
    return row_sums, col_sums, diag_sums, all_equal
magic_square = create_magic_square()
print("Original Magic Square:")
print(magic_square)
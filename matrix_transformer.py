def transpose_matrix(matrix: list[list[int | float]]) -> list[list[int | float]]:
    """Transposes a 2D matrix (swaps rows and columns)."""
    if not matrix or not matrix[0]:
        return []
    return [[matrix[r][c] for r in range(len(matrix))] for c in range(len(matrix[0]))]

def rotate_matrix_90(matrix: list[list[int | float]]) -> list[list[int | float]]:
    """Rotates a square 2D matrix 90 degrees clockwise."""
    if not matrix or not matrix[0]:
        return []
    return [list(reversed(col)) for col in transpose_matrix(matrix)]

if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original Matrix:")
    for row in mat:
        print(row)

    print("\nRotated 90° Clockwise:")
    for row in rotate_matrix_90(mat):
        print(row)

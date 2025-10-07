arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(len(arr)**0.5)
matrix = [arr[i:i+n] for i in range(0, len(arr), n)]

diagonal = [matrix[i][i] for i in range(n)]
print("Diagonal elements are", diagonal)
print("Sum of diagonal elements =", sum(diagonal))

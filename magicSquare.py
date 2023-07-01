print("This program works for odd numbers and will generate the corresponding magic square for that number.")

# Input the number
n = int(input("Enter number: "))

def generateSquare(n):
    # Create an empty magic square of size n x n
    magicSquare = [[0 for x in range(n)] for y in range(n)]

    # Initialize the position of 1
    i = n // 2
    j = n - 1

    # Fill the magic square by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:  # Wrap around conditions
            j = n - 2
            i = 0
        else:
            # If the next number goes out of the right side of the square
            if j == n:
                j = 0
            # If the next number goes out of the upper side of the square
            if i < 0:
                i = n - 1

        if magicSquare[int(i)][int(j)]:  # If the position is already filled
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1

        j = j + 1
        i = i - 1

    # Printing the magic square
    print("Magic Square for n =", n)
    print("Sum of each row or column:", n * (n * n + 1) // 2, "\n")

    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (magicSquare[i][j]), end='')

            # To display output in matrix form
            if j == n - 1:
                print()

# Generate and print the magic square
generateSquare(n)

def print_pyramid(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end=" ")
        print()

shape = 5
print_pyramid(shape)
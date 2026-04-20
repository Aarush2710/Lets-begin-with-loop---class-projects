n = int(input("Enter the no of rows : "))

for i in range(n, 0, -1): # outloop for lines

    for j in range(n - i): # spaces

        print(" ", end="")

    for k in range(2 * i - 1): # stars

        print("*", end="")

    print("")
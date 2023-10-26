def fibonacci_sequence(n):
    string = " "
    f1 = 1
    f2 = 1
    string = string + str(f1) +", " + str(f2) +", "
    for i in range(2, n):
        next_number = int(f1) + int(f2)
        string = string + str(next_number) + ", "
        f1 = f2
        f2 = int(next_number)
    string1 = string[:-2]
    print(string1)

n = 10
fibonacci_sequence(n)

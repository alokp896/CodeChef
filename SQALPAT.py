def square_pattern(n):
    count = 1
    for i in range(1, n+1):
        if i%2 != 0:
            for j in range(0, 5):
                print(count, end=" ")
                count = count + 1
        else:
            count2 = count + 4
            for n in range(0, 5):
                print(count2, end=" ")
                count2 = count2 - 1
                count = count + 1
        print("\r")

try:
    n = int(input())
    if n > 0:
        square_pattern(n)
except:
    print("")

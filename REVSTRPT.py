# cook your dish here
def pypart2(n):
    k = n
    for i in range(0, n):
        for j in range(0, k-1):
            print(end=" ")
        k= k-1
        for n in range(0,i+1):
            print("*", end="")
        print("\r")

try:
    n = int(input())
    if n > 0:
        pypart2(n)
except:
    print("")

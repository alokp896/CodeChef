def raju_trip(N):
    divisible_five = N%5
    divisible_eleven = N%6
    
    if divisible_five == 0 or divisible_eleven == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    try:
        input1 = int(input())
        raju_trip(input1)
    except:
        print("")

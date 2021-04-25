def divisible_check(N):
    divisible_five = N%5
    divisible_eleven = N%11
    
    if divisible_five == 0 and divisible_eleven == 0:
        print("BOTH")
    elif (divisible_five == 0 or divisible_eleven == 0) and (divisible_eleven + divisible_five) > 0:
        print("ONE")
    else:
        print("NONE")

if __name__ == '__main__':
    try:
        input1 = int(input())
        divisible_check(input1)
    except:
        print("")

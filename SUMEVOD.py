def sum_odd_even(n, list1):
    list1.append(n*n)
    list1.append(n * (n + 1))
    list1 = list(map(str,list1))
    print(" ".join(list1))

if __name__ == '__main__':
    n = int(input())
    if n > 0:
        sum_odd_even(n, list1 =[])
    else:
        print("")

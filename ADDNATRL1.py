def sum_natural(N, list1):
    list1.append((N*(N+1))/2)
    list1 = list(map(int,list1))
    print(list1[0])

if __name__ == '__main__':
    try:
        N = int(input())
        if N > 0:
            sum_natural(N, list1 =[])
        else:
            print(N)
    except:
        print("")

def dis_factor(N, list1):
    for I in range(1,N+1):
        dis_factor_count = N%I
        if dis_factor_count == 0:
            list1.append(I)
        else:
            continue
    list1 = list(map(str,list1))
    print(len(list1))
    print(" ".join(list1))


if __name__ == '__main__':
    try:
        N = int(input())
        dis_factor(N, list1=[])
    except:
        print("")

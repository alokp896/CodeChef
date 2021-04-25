def range_odd(L, R, list1):
    for I in range(L, R+1):
        if I%2 != 0:
            list1.append(I)
        else:
            continue
    list1 = list(map(str, list1))
    print(" ".join(list1))

if __name__ == '__main__':
    try:
        L, R = map(int, input().split())
        range_odd (L ,R, list1=[])
    except:
        print("")

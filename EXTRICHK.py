def triangle_type(a ,b ,c):
    list1 = sorted([a , b, c])
    if (list1[0]+list1[1]) > list1[2]:
        if a == b and b == c:
            print(1)
        elif (a == b and a != c) or (b == c and c != a) or ( a== c and a != b):
            print(2)
        elif ( a!= b and a!=c and b != c):
            print (3)
    else:
        print("-1")


if __name__ == '__main__':
    try:
        a, b, c = map(int, input().split())
        if a > 0 and b > 0 and c > 0:
            triangle_type(a ,b ,c)
        else:
            print("-1")
    except:
        print("")

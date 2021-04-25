def triangle_angle(a ,b ,c):
    list1 = sorted([a , b, c])
    if (list1[0]+list1[1]+list1[2]) == 180:
        print("YES")      
    else:
        print("NO")


if __name__ == '__main__':
    try:
        a, b, c = map(int, input().split())
        if a > 0 and b > 0 and c > 0:
            triangle_angle(a ,b ,c)
        else:
            print("NO")
    except:
        print("")

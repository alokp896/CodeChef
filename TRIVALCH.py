def valid_triangle(list1):
    if (list1[1]+list1[0]) > list1[2]:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    try:
        list1 = list(map(int, input().split()))
        list1 = sorted(list1)
        valid_triangle(list1)
    except:
        print("")

def thief_run(N, M, x, y, a, b):
    print("start")
    if N == x and M == y:
        print("YES")
    elif x == a and y == b:
        print("NO")
    else:
        total_cell = N+M
        Thief_required = total_cell^2 - (x+y)^2
        police_required = total_cell^2 - (a+b)^2
        if Thief_required > police_required:
            print("NO")
        elif Thief_required == police_required:
            print("YES")
        elif Thief_required < police_required:
            print("YES")
            

if __name__ == '__main__':
    try:
        list1 = []
        list2 = []
        T = int(input())

        for j in range(0, T):
            N, M = map(int, input().split())
            x, y = map(int, input().split())
            a, b = map(int, input().split())
            thief_run(N, M, x, y, a, b)
    except:
        print("")

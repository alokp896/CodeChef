def thief_run(N, M, x, y, a, b):
    print("start")
    if N == x and M == y:
        print("YES")
    elif x == a and y == b:
        print("NO")
    else:
        def check(a , b, x ,y):
            if N == x and M == y:
                x = N
                y = M
                a = N
                b = M
                print("YES")
                return x,y,a,b
            elif x == a and y == b:
                x = N
                y = M
                a = N
                b = M
                print("NO")
                return x,y,a,b
            elif N == a and M == b:
                x = N
                y = M
                a = N
                b = M
                print("NO")
                return x,y,a,b
            else:
                return x,y,a,b

        while (x != N or y != M) and (a != N or b != M):
            if (x > y and a > b) or (x == y and y < M) or (a == b and b < M):
                y = y +1
                b = b + 1
                x,y,a,b = check(a , b, x ,y)
                pass
            elif x < y and a > b:
                x = x+1
                b = b+1
                x,y,a,b = check(a , b, x ,y)
                pass
            elif x > y and a < b:
                y = y+1
                a = a+1
                x,y,a,b = check(a , b, x ,y)
                pass
            elif (x < y and a < b) or (x == y and x < N) or (a == b and a < N):
                x = x+1
                a = a+1
                x,y,a,b = check(a , b, x ,y)
                pass


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

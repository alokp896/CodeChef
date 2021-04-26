def boat_making(X, Y, xr, yr, D):
    X_per_day = int(X/D)
    Y_per_day = int(Y/D)
    if xr <= X_per_day and yr <= Y_per_day:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    try:
        T = int(input())
        for j in range(0, T):
            X, Y, xr, yr, D = map(int, input().split())
            if X > 0 and Y > 0 and D > 0:
                boat_making(X, Y, xr, yr, D)
            else:
                print("NO")
    except:
        print("")

def find_number(N, K, list1):
    if K in list1:
        print(1)
    else:
        print(-1)
         

if __name__ == '__main__':
    try:
        N, K = map(int, input().split())
        list1 = list(map(int, input().split()))
        find_number (N, K, list1)
    except:
        print("")

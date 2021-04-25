def reverse_number(list1):
    #list1 = list(map(str, list1[::-1]))
    print(" ".join(list(map(str, list1[::-1]))))        

if __name__ == '__main__':
    try:
        N = int(input())
        list1 = list(map(int, input().split()))
        reverse_number (list1)
    except:
        print("")

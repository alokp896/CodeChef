# cook your dish here
def count_cost(a, b, x, y):
    m = a*x + b*y
    print(m)

if __name__ == '__main__':
    try:
        input1 = input()
        lst = list(map(int, input1.split()))
        if len(lst) < 4:
            count_cost(0, 0, 0, 0)
        else:
            count_cost(lst[0], lst[1], lst[2], lst[3])
    except:
        print()

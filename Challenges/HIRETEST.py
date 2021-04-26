# cook your dish here
from collections import Counter
def pass_mark(X, Y, grade, list2):
    for i in range(len(grade)):
        count_word = Counter(grade[i])
        if count_word['F'] >= X or ( count_word['F'] >= (X-1) and count_word['P'] >= Y):
            list2.append(1)
        else:
            list2.append(0)
    list2 = list(map(str, list2))
    print("".join(list2))

if __name__ == '__main__':
    try:
        list1 = []
        list2 = []
        T = int(input())

        for j in range(0, T):
            N, M = map(int, input().split())
            X, Y = map(int, input().split())
            for k in range(0, N):
                grade = str(input())
                list1.append(grade)
            pass_mark(X, Y, list1, list2 = [])
            list1 = []
    except:
        print("")


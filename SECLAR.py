def largest_number(N_list):
    N_list = sorted(N_list)
    print(N_list[1])

if __name__ == '__main__':
    try:
        N_list = list()
        i = 3
        for T in range(3):
            N = int(input())
            N_list.append(N)
        largest_number(N_list)
    except:
        print("")
            

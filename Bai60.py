def KiemTra(string):
    for i in range(0, len(string)):
        for j in range(i+1,len(string)):
            if int(string[j]) < int(string[i]):
                return 0
    return -1
#=======================================
def main():
    string = input('Nhập vào một dãy số: ')
    if KiemTra(string) == 0:
        print('Dãy số không tăng dần')
    else:
        print('Dãy số tăng dần')
#=======================================
if __name__ == '__main__':
    main()


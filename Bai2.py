def Nhap():
    while(True):
        n = int(input('Moi nhap (n > 0) n = '))
        if n > 0:
            return n
        print('Nhap sai, xin vui lòng nhâp lai: ')
#================================
def TinhTong(n):
    s = 0
    for i in range(1, n + 1):
        s += i*i
    return s;
#================================
def main():
    n = Nhap()
    t = TinhTong(n)
    print('Ket qua = %d' %t)
#================================
if __name__ == '__main__':
    main()

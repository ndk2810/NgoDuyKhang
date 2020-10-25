def Nhap():
    while(True):
        n = int(input('Moi nhap (n > 0) n = '))
        if n > 0:
            return n
        print('Nhap sai, xin vui lòng nhâp lai: ')
#=======================================
def TinhTich(n):
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p;
#=======================================
def main():
    n = Nhap()
    t = TinhTich(n)
    print('Ket qua = %d' %t)
#=======================================
if __name__ == '__main__':
    main()

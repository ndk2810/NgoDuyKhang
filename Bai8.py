def Nhap():
    while(True):
        n = int(input('Moi nhap (n > 0) n = '))
        if n > 0:
            return n
        print('Nhap sai, xin vui lòng nhâp lai: ')
#=======================================
def TinhTong(n):
    s = 0.0
    for i in range(0, n + 1):
        s += (2*i+1)/(2*i+2)
    return s;
#=======================================
def main():
    n = Nhap()
    t = TinhTong(n)
    print('Ket qua = %.2f' %t)
#=======================================
if __name__ == '__main__':
    main()

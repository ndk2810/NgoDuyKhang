def Nhap():
    x = float(input('Nhập x: '))
    while(True):
        n = int(input('Moi nhap (n > 0) n = '))
        if n > 0:
            return x, n
        print('Nhap sai, xin vui lòng nhâp lai: ')
#=======================================
def TinhLuyThua(x,n):
    p = 1.0
    for i in range(1, n + 1):
        p *= x
    return p;
#=======================================
def main():
    x,n = Nhap()
    t = TinhLuyThua(x,n)
    print('Ket qua = %.2f' %t)
#=======================================
if __name__ == '__main__':
    main()

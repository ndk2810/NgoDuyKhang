def Nhap():
    x = float(input('Nhập x: '))
    while(True):
        n = int(input('Moi nhap (n > 0) n = '))
        if n > 0:
            return x, n
        print('Nhap sai, xin vui lòng nhâp lai: ')
#=======================================
def TinhTong(x,n):
    s = 0
    s1 = x
    for i in range(1, n + 1):
        s += x*x
        s1 += s
    return s1
#=======================================
def main():
    x,n = Nhap()
    t = TinhTong(x,n)
    print('Ket qua = %d' %t)
#=======================================
if __name__ == '__main__':
    main()


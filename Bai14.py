def Nhap():
    x = float(input('Nhập x: '))
    while(True):
        n = int(input('Nhập (n > 0) n = '))
        if n > 0:
            return x, n
        print('Nhập sai, xin vui lòng nhâp lai: ')
#=======================================
def TinhTong(x,n):
    s = x
    for i in range(1, n):
        s += pow(x, 2*i + 1)
    return s
#=======================================
def main():
    x,n = Nhap()
    t = TinhTong(x,n)
    print('Ket qua = %d' %t)
#=======================================
if __name__ == '__main__':
    main()


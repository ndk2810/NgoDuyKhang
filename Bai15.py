def Nhap():
    while(True):
        n = int(input('Nhập (n > 0) n = '))
        if n > 0:
            return n
        print('Nhập sai, xin vui lòng nhâp lai: ')
#=======================================
def TinhTong(n):
    s = 0
    s1 = 0
    for i in range(1, n + 1):
        s1 += i 
        s += 1/s1
    return s
#=======================================
def main():
    n = Nhap()
    t = TinhTong(n)
    print('Ket qua = %.2f' %t)
#=======================================
if __name__ == '__main__':
    main()
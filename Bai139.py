def NhapSL():
    while(True):
        n = int(input('Nhập n (n > 0): '))
        if n > 0:
            return n
        print('Bạn nhập sai, vui lòng nhập lại ...')
#===================================================
def NhapMang(n):
    a = []
    for i in range(n):
        t = float(input('a[%d] = ' %i))
        a += [t]
    return a
#===================================================
def XuatMang(a):
    for item in a:
        print('%6.2f'%item, end='')
#===================================================
def ViTriSoHoanThienDauTien(a):
    for i in range(len(a)):
        if a[i] % 2 == 0: 
            return i
    return -1
#===================================================
def main():
    n = NhapSL()
    a = NhapMang(n)
    XuatMang(a)
    m = ViTriSoHoanThienDauTien(a)
    print('\nVị trí có số hoàn thiện đầu tiên là: %d' %m)
#===================================================
if __name__ == '__main__':
    main()

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
def GiaTriDuongCuoiCung(a):
    for item in a[::-1]:
        if item > 0: 
            return item
    return -1
#===================================================
def main():
    n = NhapSL()
    a = NhapMang(n)
    XuatMang(a)
    m = GiaTriDuongCuoiCung(a)
    print('\nGía trị dương đầu tiên là: %.2f' %m)
#===================================================
if __name__ == '__main__':
    main()

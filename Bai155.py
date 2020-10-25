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
def KiemTra(a, x):
    k = a[0]
    for i in range(len(a)):
        if x-a[i] > k:
            k = a[i]
    return k
#===================================================
def main():
    n = NhapSL()
    a = NhapMang(n)
    x = float(input('Nhập x: '))
    XuatMang(a)
    SoXaNhat = abs(KiemTra(a,x))
    print('\nSố xa x nhất trong mảng là: %6.2f' %SoXaNhat)
#===================================================
if __name__ == '__main__':
    main()

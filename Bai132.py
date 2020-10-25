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
        t = int(input('a[%d] = ' %i))
        a += [t]
    return a
#===================================================
def XuatMang(a):
    for item in a:
        print('%4d'%item, end='')
#===================================================
def LietKeGiaTriChan(a):
    for item in a:
        if item % 2 == 0: 
            print('%4d'%item, end='')
#===================================================
def main():
    n = NhapSL()
    a = NhapMang(n)
    XuatMang(a)
    print('\nCác giá trị chẵn là: ')
    LietKeGiaTriChan(a)
#===================================================
if __name__ == '__main__':
    main()

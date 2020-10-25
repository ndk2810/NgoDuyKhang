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
        print('%5.2f'%item, end='')
#===================================================
def LietKeViTriGiaTriAm(a):
    for i in range(len(a)):
        if a[i] < 0: 
            print('%4d'%i, end='')
#===================================================
def main():
    n = NhapSL()
    a = NhapMang(n)
    XuatMang(a)
    print('\nCác vị trí có giá trị âm là: ')
    LietKeViTriGiaTriAm(a)
#===================================================
if __name__ == '__main__':
    main()

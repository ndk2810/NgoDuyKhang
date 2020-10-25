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
def GiaTriLonNhat(a):
    m = a[0]
    for i in range(len(a)):
        if m < a[i]: 
            m = a[i]
    return m
#===================================================
def main():
    n = NhapSL()
    a = NhapMang(n)
    XuatMang(a)
    m = GiaTriLonNhat(a)
    print('\nGía trị lớn nhất là: %.2f' %m)
#===================================================
if __name__ == '__main__':
    main()

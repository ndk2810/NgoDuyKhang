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
def main():
    n = NhapSL()
    a = NhapMang(n)
    print(a)
#===================================================
if __name__ == '__main__':
    main()

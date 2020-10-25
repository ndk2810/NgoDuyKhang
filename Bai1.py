def TinhTong(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s
#================================
def main():
    n = int(input("Nhâp n = "))
    t = TinhTong(n)
    print('Tông = %d' %t)
#================================
if __name__ == '__main__':
    main()

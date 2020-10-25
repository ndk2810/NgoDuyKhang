def UocSo(x):
    Tong = 0
    for i in range(1, x):
        if x % i == 0:
            Tong += i
    return Tong
#=======================================
def main():
    x = int(input('Nhập vào x: '))
    KetQua = UocSo(x)
    print('Tổng tất cả ước số của %d = %d' %(x, KetQua))
#=======================================
if __name__ == '__main__':
    main()
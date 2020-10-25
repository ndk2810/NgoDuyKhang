def UocSo(x):
    for i in range(1, x):
        if x % i == 0:
            print('%d là một ước số của %d' %(i, x))
#=======================================
def main():
    x = int(input('Nhập vào x: '))
    UocSo(x)
#=======================================
if __name__ == '__main__':
    main()
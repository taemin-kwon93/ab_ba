def main():
    x = int(input())
    print(-x)


def throwError():
    print('have to input integer')


try:
    main()
except:
    throwError()

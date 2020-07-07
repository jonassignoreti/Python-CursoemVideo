while True:
    v = str(input('Digite [S/N]: ')).upper()
    print(v.__contains__('S') or v.__contains__('N'))

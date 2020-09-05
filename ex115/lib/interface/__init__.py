def line(tam):
    print('-' * tam)


def title(txt, tam=0):
    if tam == 0:
        tam = len(txt) + 10
        line(tam)
        print(f'{txt:^{tam}}')
        line(tam)
    else:
        line(tam)
        print(f'{txt:^{tam}}')
        line(tam)
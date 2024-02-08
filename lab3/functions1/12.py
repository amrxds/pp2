def histogramma(x):

    for i in x:
        print('*'*i, end = '\n')

x = [ x for x in map(int, input().split())]

histogramma(x)
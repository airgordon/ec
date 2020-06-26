from functools import reduce


def h2i(x):
    return int(x.replace(' ', ''), 16)


def endianRevert(x):
    normStr = x.replace(' ', '')
    l = list(map(''.join, zip(*[iter(normStr)] * 2)))
    #print(l)
    #print(l[::-1])
    bigEndianStr = reduce((lambda x, y: x + y), l[::-1])
    return bigEndianStr


def h22i(str):
    str = str.replace(' ', '')

    f = str[0:(len(str) // 2)]
    s = str[(len(str) // 2):]

    return h2i(f), h2i(s)


def lh22i(str):
    str = str.replace(' ', '')

    f = str[0:(len(str) // 2)]
    s = str[(len(str) // 2):]

    return endianRevert(f), endianRevert(s)
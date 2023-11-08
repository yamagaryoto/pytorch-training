from utils.function import add

def count_word(st, wr):
    ret = 0
    for i in range(len(st)):
        if wr == st[i]:
            ret = add(ret, 1)
    return ret

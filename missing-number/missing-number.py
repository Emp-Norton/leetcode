def f(n):
    max = len(n)
    sn = sorted(n)
    for i,v in enumerate(sn):
            if i != v:
                    return i
    return max

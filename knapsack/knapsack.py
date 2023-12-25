import itertools  


def maximum_value(maximum_weight, items):
    ruk = maximum_weight
    sp1 = items
    itog = 0

    for i in range(1, len(sp1)+1):
        for j in list(itertools.combinations(sp1, i)):
            ves = sum(k['weight'] for k in j)
            vall = sum(m['value'] for m in j)
            if ves <= ruk and vall > itog:
                itog = vall 
    
    return itog

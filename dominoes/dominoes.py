def can_chain(dominoes):
    if dominoes == []:
        return []
    elif len(dominoes) == 1:
        if dominoes[0][0] == dominoes[0][-1]:
            return dominoes
        else:
            return None
    else:
        d1 = [list(x) for x in dominoes]
        lend1 = len(d1)
        res1 = [] # - osnovnoy

        for k in d1:
            res2 = []
            d2 = d1.copy()
            res2.append(k)
            d2.remove(k)

            for _ in range(len(d1)**2):
                for i in d2:
                    if i[0] == res2[-1][1]:
                        res2.append(i)
                        d2.remove(i)
                    elif i[1] == res2[-1][1]:
                        res2.append([i[1], i[0]])
                        d2.remove(i)
                    elif i[1] == res2[0][0]:
                        res2.insert(0, i)
                        d2.remove(i)
                    elif i[0] == res2[0][0]:
                        res2.insert(0, [i[1], i[0]])
                        d2.remove(i)

            res1.append(res2)

        sp3 = []
        for i in res1:
            if i[0][0] == i[-1][1] and len(i) == lend1:
                sp3.append(i)

        sp5 = []
        if sp3:
            sp5 = sp3[0]
        
        # sp4 = [tuple(m) for m in sp3[0]]
        sp4 = []
        if sp5:
            for i in sp5:
                sp4.append(tuple([i[0], i[1]]))
        else: 
            sp4 = None

        # print(sp4)

        return sp4

####################################################################

a = [
            (1, 2),
            (5, 3),
            (3, 1),
            (1, 2),
            (2, 4),
            (1, 6),
            (2, 3),
            (3, 4),
            (5, 6),
        ]
print(can_chain(a))

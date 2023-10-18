def transpose(lines_st):
    lines = lines_st.split('\n')
    new_b = []
    itog_mas = []
    ind = 0

    max_len = (max([len(x) for x in lines]))

    for i in lines:
        if len(i) < max_len:
            new_b.append(i+((max_len - len(i))*'*'))
        else:
            new_b.append(i)

    for i in range(max_len):
        b_str = ''
        for j in new_b:
            b_str += (j[ind])

        itog_mas.append(b_str)
        ind += 1

    ttt = itog_mas.copy()

    u = 0
    while u < len(ttt):
        while ttt[u][-1] == '*':
            ttt[u] = ttt[u][:-1]
        u += 1

    zk = 0
    for rr in ttt:
        if '*' in rr:
            ttt[zk] = rr.replace('*', ' ')
        zk += 1

    return '\n'.join(ttt)


# ww = ["The longest line.", "A long line.", "A longer line.", "A line."]
# print(transpose("\n".join(ww)))

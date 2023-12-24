def encode(message, rails):
    mass = []

    for i in range(rails):
        mass.append(['*'] * len(message))

    i1 = 0
    i2 = 0
    step = 1

    for i in message:
        mass[i1][i2] = i

        i2 += 1
        i1 += step
        if i1 == rails-1:
            step *= -1
        if i1 == 0:
            step *= -1

    for i in mass:
        while '*' in i:
            i.remove('*')

    return ''.join(sum(mass, []))

# ********************************************************


def decode(encoded_message, rails):
    s_st = encoded_message
    mas = encoded_message
    s_sp = list(encoded_message)
    res = []

    for _ in range(rails):
        res.append([])

    ii = 1
    for i in range(len(s_sp)):

        if ii == 1:
            for i in range(rails):
                if s_st:
                    res[i] += s_st[0]
                    s_st = s_st[1:]

                    for k in range(rails):
                        if k != i:
                            res[k].append('*')
            ii = 2

        if ii == 2:
            for j in range(rails-2, 0, -1):
                if s_st:
                    res[j] += s_st[0]
                    s_st = s_st[1:]

                    for k in range(rails):
                        if k != j:
                            res[k].append('*')
            ii = 1

    r = []
    for i in range(len(res)):
        r.append([])

    s = 0
    while s < len(res):
        for i in res[s]:
            if i != '*':
                r[s].append(mas[0])
                mas = mas[1:]
            else:
                r[s].append('*')
        s += 1

    #   *************************************************************

    result = ''
    t = 0
    ik = 1
    for _ in range(len(encoded_message)):

        if ik == 1:
            for i in range(rails):
                if t < len(encoded_message):
                    result += r[i][t]
                    t += 1

            ik = 2

        if ik == 2:
            for j in range(rails-2, 0, -1):
                if t < len(encoded_message):
                    result += r[j][t]
                    t += 1

            ik = 1

    return result

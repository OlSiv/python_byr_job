def commands(binary_str):
    #bi = str(bin(int(binary_str)))
    #print(bi)
    bi = binary_str
    res = []

    if bi[-1] == '1':
        res.append('wink')

    if bi[-2] == '1':
        res.append('double blink')

    if bi[-3] == '1':
        res.append('close your eyes')

    if bi[-4] == '1':
        res.append('jump')
        

    return res if bi[-5] != '1' else res[::-1]

def best_hands(hands):
    h = hands 
    res = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    obr = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

    for i in h:
        if ((('A' in i) and ('K' in i) and ('Q' in i) and ('J' in i) and ('10' in i)) and (
                i.count('S') == 5 or i.count('C') == 5 or i.count('H') == 5 or i.count('D') == 5)):
            res[0].append(i)

        elif ((i.count('S') == 5) or (i.count('C') == 5) or (i.count('H') == 5) or (i.count('D') == 5)) and (
              (('2' in i) and ('3' in i) and ('4' in i) and ('5' in i) and ('6' in i)) or (
              ('3' in i) and ('4' in i) and ('5' in i) and ('6' in i) and ('7' in i)) or (
              ('4' in i) and ('5' in i) and ('6' in i) and ('7' in i) and ('8' in i)) or (
              ('5' in i) and ('6' in i) and ('7' in i) and ('8' in i) and ('9' in i)) or (
              ('6' in i) and ('7' in i) and ('8' in i) and ('9' in i) and ('10' in i)) or (
              ('7' in i) and ('8' in i) and ('9' in i) and ('10' in i) and ('J' in i)) or (
              ('8' in i) and ('9' in i) and ('10' in i) and ('J' in i) and ('Q' in i)) or (
              ('9' in i) and ('10' in i) and ('J' in i) and ('Q' in i) and ('K' in i)) or (
              ('10' in i) and ('J' in i) and ('Q' in i) and ('K' in i) and ('A' in i))):
            res[1].append(i)

        elif ((i.count('S') == 5) or (i.count('C') == 5) or (i.count('H') == 5) or (i.count('D') == 5)) and (
            ('2' in i) and ('3' in i) and ('4' in i) and ('5' in i) and ('A' in i)):
            res[2].append(i)

        elif (
            (i.count('2') == 4) or (
            i.count('3') == 4) or (
            i.count('4') == 4) or (
            i.count('5') == 4) or (
            i.count('6') == 4) or (             
            i.count('7') == 4) or (              
            i.count('8') == 4) or (              
            i.count('9') == 4) or (    
            i.count('10') == 4) or (              
            i.count('J') == 4) or (          
            i.count('Q') == 4) or (
            i.count('K') == 4) or (
            i.count('A') == 4)):
            res[3].append(i)

        elif 3 in [(i.count(x[0])) for x in i.split()] and 2 in [(i.count(x[0])) for x in i.split()]:
            res[4].append(i)

        elif ((i.count('S') == 5) or (i.count('C') == 5) or (i.count('H') == 5) or (i.count('D') == 5)):
            res[5].append(i)

        elif (
              (('2' in i) and ('3' in i) and ('4' in i) and ('5' in i) and ('6' in i)) or (
              ('3' in i) and ('4' in i) and ('5' in i) and ('6' in i) and ('7' in i)) or (
              ('4' in i) and ('5' in i) and ('6' in i) and ('7' in i) and ('8' in i)) or (
              ('5' in i) and ('6' in i) and ('7' in i) and ('8' in i) and ('9' in i)) or (
              ('6' in i) and ('7' in i) and ('8' in i) and ('9' in i) and ('10' in i)) or (
              ('7' in i) and ('8' in i) and ('9' in i) and ('10' in i) and ('J' in i)) or (
              ('8' in i) and ('9' in i) and ('10' in i) and ('J' in i) and ('Q' in i)) or (
              ('9' in i) and ('10' in i) and ('J' in i) and ('Q' in i) and ('K' in i)) or (
              ('10' in i) and ('J' in i) and ('Q' in i) and ('K' in i) and ('A' in i)) 
            #   or (
            #   ('2' in i) and ('3' in i) and ('4' in i) and ('5' in i) and ('A' in i))
              ):
            res[6].append(i)

        elif ('2' in i) and ('3' in i) and ('4' in i) and ('5' in i) and ('A' in i):
            res[7].append(i)

        elif 3 in [(i.count(x[0])) for x in i.split()]:
            res[8].append(i)

        # two pars -
        elif (((i.count('2') == 2) and (
            (i.count('3') == 2) or (
            i.count('4') == 2) or (
            i.count('5') == 2) or (
            i.count('6') == 2) or (
            i.count('7') == 2) or (
            i.count('8') == 2) or (
            i.count('9') == 2) or (
            i.count('10') == 2) or (
            i.count('J') == 2) or (
            i.count('Q') == 2) or (
            i.count('K') == 2) or (
            i.count('A') == 2)
            )) or (
                (i.count('3') == 2) and ((
            i.count('4') == 2) or (
            i.count('5') == 2) or (
            i.count('6') == 2) or (
            i.count('7') == 2) or (
            i.count('8') == 2) or (
            i.count('9') == 2) or (
            i.count('10') == 2) or (
            i.count('J') == 2) or (
            i.count('Q') == 2) or (
            i.count('K') == 2) or (
            i.count('A') == 2))
            ) or (
                 (i.count('4') == 2) and ((
            i.count('5') == 2) or (
            i.count('6') == 2) or (
            i.count('7') == 2) or (
            i.count('8') == 2) or (
            i.count('9') == 2) or (
            i.count('10') == 2) or (
            i.count('J') == 2) or (
            i.count('Q') == 2) or (
            i.count('K') == 2) or (
            i.count('A') == 2))
            ) or (
                 (i.count('5') == 2) and ((
            i.count('6') == 2) or (
            i.count('7') == 2) or (
            i.count('8') == 2) or (
            i.count('9') == 2) or (
            i.count('10') == 2) or (
            i.count('J') == 2) or (
            i.count('Q') == 2) or (
            i.count('K') == 2) or (
            i.count('A') == 2))
            ) or (
                 (i.count('6') == 2) and ((
            i.count('7') == 2) or (
            i.count('8') == 2) or (
            i.count('9') == 2) or (
            i.count('10') == 2) or (
            i.count('J') == 2) or (
            i.count('Q') == 2) or (
            i.count('K') == 2) or (
            i.count('A') == 2))
            ) or (
                 (i.count('7') == 2) and ((
            i.count('8') == 2) or (
            i.count('9') == 2) or (
            i.count('10') == 2) or (
            i.count('J') == 2) or (
            i.count('Q') == 2) or (
            i.count('K') == 2) or (
            i.count('A') == 2))
            ) or (
                 (i.count('8') == 2) and ((
            i.count('9') == 2) or (
            i.count('10') == 2) or (
            i.count('J') == 2) or (
            i.count('Q') == 2) or (
            i.count('K') == 2) or (
            i.count('A') == 2))
            ) or (
                 (i.count('9') == 2) and ((
            i.count('10') == 2) or (
            i.count('J') == 2) or (
            i.count('Q') == 2) or (
            i.count('K') == 2) or (
            i.count('A') == 2))
            ) or (
                 (i.count('10') == 2) and ((
            i.count('J') == 2) or (
            i.count('Q') == 2) or (
            i.count('K') == 2) or (
            i.count('A') == 2))
            ) or (
                 (i.count('J') == 2) and ((
            i.count('Q') == 2) or (
            i.count('K') == 2) or (
            i.count('A') == 2))
            ) or (
                 (i.count('Q') == 2) and ((
            i.count('K') == 2) or (
            i.count('A') == 2))
            ) or (
                 (i.count('K') == 2) and (i.count('A') == 2))):
            res[9].append(i)
            
        elif 2 in [(i.count(x[0])) for x in i.split()]:
            res[10].append(i)

        # - star card - 
        else:
            res[11] = h


    if res[11] != []:
        for j in obr:
            if j in (','.join(res[11])):
                for i in res[11]:
                    if j not in i:
                        res[11].remove(i)
                break 

    # - 4-ka -
    if len(res[3]) > 1:
        for j in obr:
            if ','.join(res[3]).count(j) >= 4:
                for i in res[3]:
                    if i.count(j) < 4:
                        res[3].remove(i)

    # - 3 and 2 po max 3-ke -
    if len(res[4]) > 1:
        for j in obr:
            if ','.join(res[4]).count(j) >= 3:
                for i in res[4]:
                    if i.count(j) < 3:
                        res[4].remove(i)

    # - para po max 2-ke -
    if len(res[10]) > 1:
        for j in obr:
            if ','.join(res[10]).count(j) >= 2:
                for i in res[10]:
                    if i.count(j) < 2:
                        res[10].remove(i)

    # - 2 pari po max 2-ke v pare -
    if len(res[9]) > 1:
        for j in obr:
            if ','.join(res[9]).count(j) >= 2:
                for i in res[9]:
                    if i.count(j) < 2:
                        res[9].remove(i)


    reso = []
    for i in res:
        if i != []:
            reso.append(i)
            break

    resss = reso[0]

        
    for j in obr:
        if j in (','.join(resss)):
            for i in resss:
                if j not in i:
                    resss.remove(i)
    

    return resss

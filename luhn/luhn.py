class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        st = self.card_num.replace(' ', '')

        if not st.isdigit():
            return False
        elif st == '0':
            return False
        else:
            st2 = st[::-1]
            sp1 = []
            sp2 = []
            sp3 = list(st2)

            for i in sp3[::2]:
                sp1.append(int(i))

            sp4 = sp3[1:]
            for i in sp4[::2]:
                sp2.append(i)

            sp5 = []
            for i in sp2:
                if (int(i) * 2) > 9:
                    sp5.append(int(i) * 2 - 9)
                else:
                    sp5.append(int(i) * 2)

            spp = sum(sp1 + sp5)

            return spp % 10 == 0


#print(Luhn("234 567 891 234").valid())

class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        self.item = item 
        list_res = self.lst
        return self.item in list_res

    @property
    def lst(self):
        zn1 = self.score
        zn = 0
        sp = []
        delitel = [128, 64, 32, 16, 8, 4, 2, 1]
        aler = [
            'cats', 
            'pollen', 
            'chocolate', 
            'tomatoes', 
            'strawberries', 
            'shellfish', 
            'peanuts', 
            'eggs'
            ]
        ch = 0

        if zn1 <= 256:
            zn = zn1 
        else:
            zn = zn1 % 256

        for i in delitel:
            if zn // i == 1:
                sp.append(aler[ch])
                zn -= i
                ch +=1
            else:
                ch +=1

        return(sp)
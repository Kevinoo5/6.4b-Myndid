inp = input("Sisestage failinimi: ")
fail = open(inp)
mündid = []

def pronksikarva_summa(mündid):
    summa = (sum(mündid))
    return summa

for münt in fail:
    if int(münt) <= 5:
        mündid.append(int(münt))
    
print(pronksikarva_summa(mündid))
fail.close()

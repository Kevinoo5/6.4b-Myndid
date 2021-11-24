inp = input("Sisestage failinimi: ")
fail = open(inp)
mündid = []

def pronksikarva_summa(mündid):
    for münt in fail:
        if int(münt) <= 5:
            mündid.append(int(münt))
    summa = (sum(mündid))
    return summa

print(pronksikarva_summa(mündid))
fail.close()
f =open("input.txt","r")

symbols = ['*','#','$','@','/','+','-','_','&','§','%','=',';','?','!','^','¨']

def to_list(doc):
    liste = []
    for e in doc:
        liste.append(list(e.strip()))
    return liste

def check(l:list):
    numb, isin, dig = [], 0, []
    all = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j].isdigit():
                dig.append(l[i][j])
                print(i, j , l[i][j],dig)
                if (j+1) < len(l[i]) and l[i][j+1] in symbols :
                    isin+=1
                if (j-1) > 0 and l[i][j-1] in symbols :
                    isin+=1
                if (i+1) < len(l) and l[i+1][j] in symbols :
                    isin+=1
                if (i-1) > 0 and l[i-1][j] in symbols :
                    isin+=1
                if (i+1) < len(l) and (j+1) < len(l[i]) and l[i+1][j+1] in symbols :
                    isin+=1
                if (i+1) < len(l) and (j-1) > 0 and l[i+1][j-1] in symbols :
                    isin+=1
                if (i-1) > 0 and (j+1) < len(l[i]) and l[i-1][j+1] in symbols :
                    isin+=1
                if (i-1) > 0 and (j-1) > 0 and l[i-1][j-1] in symbols :
                    isin+=1
            else:
                if len(dig) > 0 and isin >= 1:
                    numb.append("".join(dig))
                    isin = 0
                if ("".join(dig)).isdigit():
                    all.append("".join(dig))
                dig.clear()
    return numb, all

def comparing(l1:list, l2:list):
    notIn = []
    for i in range(len(l2)):
        if not (l2[i] in l1):
            notIn.append(l2[i])
    return notIn

l1, l2 = check(to_list(f))
print(l1,l2)
print(comparing(l1,l2))
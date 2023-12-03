f = open("input.txt", "r")

def findInLine(line:str):
    liste, numb = list(line), []
    for e in liste:
        if ord(e) <= 57 and ord(e) >= 48:
            if len(numb) == 2:
                numb[1] = str(e)
            else:
                numb.append(str(e))
    if len(numb) == 1:
        numb.append(str(numb[0]))
    return int("".join(numb))

def result():
    result = 0
    for lines in f:
        result += findInLine(lines)
    return result

print(result())
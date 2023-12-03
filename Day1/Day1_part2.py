valid_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
f = open("input3.txt", "r")

def Convert_String_Digits_To_Int(digits:str):
    new_digits = valid_digits[digits]
    return new_digits

def All_To_String(liste:list):
    new_liste = []
    for e in liste:
        new_liste.append(str(e))
    return new_liste

def Int_To_Int(line:str):
    liste_number = list(line)
    new_line = []
    for e in liste_number:
        if ord(e) <= 57 and ord(e) >= 48:
            new_line.append(int(e))
        else:
            new_line.append(e)
    return new_line

def findInLine(line:str):
    liste_number, number = Int_To_Int(line), []
    size = len(liste_number)
    for o in range(len(liste_number)):
        e = liste_number[o]
        i = o
        if type(e) == str:
            word = []
            while i < size and type(liste_number[i]) == str:
                word.append(liste_number[i])
                i+=1
                if "".join(word) in valid_digits:
                    if not ("".join(word) in number):
                        number.append("".join(word))
            i+=1
        else:
            number.append(e)
    new_liste = []
    for e in number:
        if type(e) == str:
            new_liste.append(Convert_String_Digits_To_Int(e))
        else:
            new_liste.append(e)
    r = All_To_String(new_liste)
    first = r[0]
    last = r[-1]
    return int(first+last)

def result():
    result = 0
    for lines in f:
        result += findInLine(lines)
        print(result)
    return result

print(result()==54728)
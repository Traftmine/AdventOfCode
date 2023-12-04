cubes = [12,13,14]

f = open("input.txt",'r')

def Get_Hands(line:str):
    line_split_without_id = "".join(line.replace(",","").split(':')[1::])
    hands = line_split_without_id.replace(";"," ;")
    return hands

def Get_Game_Id(line:str):
    line_split = line.split(':')
    game_id = int(line_split[0].split()[1])
    return game_id

def Int_To_Int(line:str):
    liste_number = line.split()
    new_line = []
    for e in liste_number:
        if e.isdigit():
            new_line.append(int(e))
        else:
            new_line.append(e)
    return new_line

def compare(liste:list):
    size = len(liste)
    i = 0
    red, green, blue = [],[],[]
    while i < size:
        if type(liste[i+1]) == int or (liste[i+1]) == ';':
            i+=1
        elif liste[i+1] == 'red':
            red.append(liste[i])
        elif liste[i+1] == 'green':
            green.append(liste[i])
        elif liste[i+1] == 'blue':
            blue.append(liste[i])
        if i == size-2:
            return [max(red),max(green),max(blue)]
        elif liste[i+2] == ';':
            i+=3
        else:
            i+=2
    return [max(red),max(green),max(blue)]

def test(line):
    print("Game ID " + str(Get_Game_Id(line)))
    print(compare(Int_To_Int(Get_Hands(line))))
    print(Int_To_Int(Get_Hands(line)))

def main():
    result = 0
    for lines in f:
        line = lines.strip()
        print("Game ID " + str(Get_Game_Id(line)))
        list_max = compare(Int_To_Int(Get_Hands(line)))
        result+= list_max[0]*list_max[1]*list_max[2]
        print(result)
    return result

main()
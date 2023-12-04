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
    while i < size:
        if type(liste[i+1]) == int or (liste[i+1]) == ';':
            i+=1
        elif liste[i+1] == 'red':
            if liste[i] > cubes[0]:
                print("Impossible red")
                return False
        elif liste[i+1] == 'green':
            if liste[i] > cubes[1]:
                print("Impossible green")
                return False
        elif liste[i+1] == 'blue':
            if liste[i] > cubes[2]:
                print("Impossible blue")
                return False
        else:
            print("BIZARRE")
            return False
        if i == size-2:
            return True
        elif liste[i+2] == ';':
            i+=3
        else:
            i+=2
    return True

def test(line):
    print("Game ID " + str(Get_Game_Id(line)))
    print(compare(Int_To_Int(Get_Hands(line))))
    print(Int_To_Int(Get_Hands(line)))

def main():
    result = 0
    for lines in f:
        line = lines.strip()
        print("Game ID " + str(Get_Game_Id(line)))
        if compare(Int_To_Int(Get_Hands(line))):
            result+=Get_Game_Id(line)
        print(result)
    return result
main()
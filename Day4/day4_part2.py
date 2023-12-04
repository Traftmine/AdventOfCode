f = open("input.txt",'r')

#line = (" ".join(f.readline().strip().split()[2::])).split("|")
#first, second = line[0].split(), line[1].split()

def check(input:list,output:list):
    cmpt = 0
    for e in input:
        if output.count(e) >= 1:
            cmpt+=1
    return cmpt

def main():
    result, line_nb, toAdd = [], 0, 0
    for lines in f:
        line = (" ".join(lines.strip().split()[2::])).split("|")
        first, second = line[0].split(), line[1].split()
        nb = check(first,second)
        print("new line" + " resultat : " + str(nb))
        if len(result) > line_nb:
            print("toAdd : " + str(toAdd))
            toAdd = result[line_nb]
        for i in range(nb):
            if result == []:
                result.append(1)
            elif i >= len(result):
                result.append(1)
            else:
                result[line_nb+i]+= toAdd
        print(result)
        line_nb +=1
    

main()
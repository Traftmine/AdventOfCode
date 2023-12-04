f = open("input.txt",'r')

def check(input:list,output:list):
    cmpt = 0
    for e in input:
        if output.count(e) >= 1:
            if cmpt == 0:
                cmpt += 1
            else:
                cmpt *=2
    return cmpt

def main():
    result = 0
    for lines in f:
        line = (" ".join(lines.strip().split()[2::])).split("|")
        first, second = line[0].split(), line[1].split()
        result += check(first,second)
    print(result)

main()
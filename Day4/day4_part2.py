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
    result, line_nb = [], 0
    for lines in f:
        line = (" ".join(lines.strip().split()[2::])).split("|")
        first, second = line[0].split(), line[1].split()
        result_line = [0 for i in range(len(first))]
        nb = check(first,second)
        print("new line" + " resultat : " + str(nb))
        result = result_line.copy()
        for i in range(nb):
            if result[line_nb+i+1] == 0:
                result_line[line_nb+i+1] += 1
            else:
                result_line[line_nb+i+1] += result[line_nb+i+1]
        line_nb +=1
        print(result_line)

main()
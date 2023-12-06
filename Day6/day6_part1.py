f = open("input.txt","r")

time = f.readline().strip().split()[1::]
dist = f.readline().strip().split()[1::]

def ways(t : int, d : int):
    w = 0
    for i in range(t):
        new_t = t - i
        if i*new_t > d:
            w+=1
    return w

def main(t : list, d : list):
    res = 1
    for i in range(len(t)):
        res *= ways(int(t[i]),int(d[i]))
    return res

print("Result : " + str(main(time, dist)))
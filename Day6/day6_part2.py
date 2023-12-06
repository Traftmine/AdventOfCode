f = open("input.txt","r")

time = "".join(f.readline().strip().split()[1::])
dist = "".join(f.readline().strip().split()[1::])

def ways(t : int, d : int):
    w = 0
    for i in range(t):
        new_t = t - i
        if i*new_t > d:
            w+=1
    return w

print("Result : " + str(ways(int(time), int(dist))))
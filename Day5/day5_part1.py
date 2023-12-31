from operator import itemgetter

f = open("input.txt","r")

seeds_soil = {}
map_liste = []

def get_seeds(line:str):
    return line.strip().split(':')[1].split()

def convert(soil:list):
    for e in soil[1::]:
        esplit = e.split()
        dest, src, rg = int(esplit[0]), int(esplit[1]), int(esplit[2])
        dest_list = [i for i in range(dest,dest+rg)]
        src_list = [i for i in range(src,src+rg)]
        for i in range(rg):
            if dest_list[i] not in seeds_soil:
                seeds_soil[src_list[i]] = dest_list[i]
    return 0

def get_map_liste(f):
    mape = []
    for e in f:
        if not e.isspace():
            mape.append(e.strip())
        else:
            map_liste.append(mape)
            mape = []
    return map_liste[1::]

def main():
    map_liste = get_map_liste(f)
    for e in map_liste:
        convert(e)
    print(seeds_soil.get(50))
    return 0

main()
print(seeds_soil)
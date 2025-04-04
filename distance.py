distances = {
    "Voyager 1":163,
    "voyager 2":136,
    "Pioneer 10":80,
    "New Horizon":50,
    "Pioneer 11":44
}

def main():
    #for name in distances.keys():
        #print(f"{name} is {convert(distances[name])}  meter from Earth")
    for name in distances.values():
        print(f"{name} is {convert(name)}  meter from Earth")

def convert(au):
    return au * 149597870700
main()

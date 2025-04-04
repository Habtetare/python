def main():
    spacecarft = {"Name":"James webb Space Telescope","Distance":None}
    spacecarft.update({"orbit":"sun"})
    print(create_report(spacecarft))

def create_report(spacecarft):
    return f"""
    ============ Report ==============

    Name : {spacecarft.get("Name","Unknown")}
    Distance : {spacecarft.get("Distance","Unknown")} AU
    Orbit : {spacecarft.get("orbit","Unknown")} 
    ==================================
    """


main()

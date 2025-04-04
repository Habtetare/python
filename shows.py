SHOWS = [
    " Avater: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron ",
    "the Proud family"
]

def main():
    cleand_shows = []
    for show in SHOWS:
        cleand_shows.append(show.title().strip())
    print(','.join(cleand_shows))


main()
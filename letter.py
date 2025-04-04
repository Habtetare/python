def main():
    Names =["Mario","Luigi","Daisy","Yoshi","Jibril"]
    for invit in Names:
       print(write_letter(invit,"Princess peach"))

def write_letter(receiver, sender):
    return f"""
        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        Dear {receiver},

        You are cordially invited to a ball at
        Peach`s Castle this evening, 7:00 PM.

        Sincerely.
        {sender}
        +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
        """

main()

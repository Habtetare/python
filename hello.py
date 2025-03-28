def main():
    Name = input("What is ur name?").strip().title()
    #print(f"Hello, {Name}")#comments 
    hello(Name)#Return Hello with passed parameted
    
def hello(to="World"):
    print(f"Hello, {to}")

main()
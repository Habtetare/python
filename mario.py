def main():
    #print_column(3)
    #print_row(3)
    print_square(4,10)

#def print_column(hight):
 #   for _ in range(hight):
 #       print("#\n" * hight)

def print_row(width):
    print("#" * width)

def print_square(hight,width):
    for i in range(hight):
        print_row(width)

main()

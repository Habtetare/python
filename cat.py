#n = int(input("Number ?"))
#i = int(0)
#while n > i:
#    print("meow")
#    i += 1

#print("meow\n" * n,end="" )

#for i in range(n):
#    print("meow")


#while True:
 #   n = int(input("Number ?"))
  #  if n < 0:
   #     continue
    #else:
     #   break
#for _ in range(n):
 #   print("meow")


def main():
 n = get_number()
 meow(n)

def get_number():
   while True:
    n = int(input("Number ?"))
    if n < 0:
        continue
    else:
        return n

def meow(n):
    for _ in range(n):
        print("meow")

main()

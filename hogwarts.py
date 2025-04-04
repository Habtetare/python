#students = ["Hermione","Harry","Ron","Draco"]

#Address = {"Hermione":"ADD",
 #          "Harry":"MQX",
  #         "Ron":"AWS",
   #        "Draco":"BJR",
    #       }
Data = [
    {"Name":"Hermione","Adr":"ADD","petronus":"Dog"},
    {"Name":"Harry","Adr":"MQX","petronus":"cat"},
    {"Name":"Ron","Adr":"AWS","petronus":"Fish"},
    {"Name":"Draco","Adr":"BJR","petronus":None},
]
#for student in students:
 #   print(student)
#for stu in range(len(students)):
 #   print(stu + 1,students[stu])

#for add in Address:
 #   print(add ,Address[add], sep=",")

for dat in Data:
     print(dat["Name"], sep=",")
    #for name in dat:
     #  print(dat[name], sep=",")

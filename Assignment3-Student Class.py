class Student:
     __StuName="Ashish"    
     __StuRollNumber=256475
     def setName(self,Name):
          self.__StuName=Name
          pass
     def getName(self):
          return self.__StuName
          pass
     def SetRollNumber(self,RollNumber):
          self.__StuRollNumber=RollNumber
          pass
     def getRollNumber(self):
          return self.__StuRollNumber
          pass
     def Student_Details(self):
         print("Student name is:",Student.__StuName)
         print("Student RollNumber is:",Student.__StuRollNumber)
  
x=Student()
x.Student_Details()
x.setName("Ashish")
x.SetRollNumber(256475)
print(x.getName())
print(x.getRollNumber())




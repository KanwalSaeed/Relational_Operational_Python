











 # GREATER THEN             >
  #LESS THEN                 <
  #GREATER THEN EQUAL TO     >=
  #LESS THEN EQUAL TO        <=
  #eQUAL TO                  ==

first_number = 20
second_number = 30
#find which one is greater.
if first_number > second_number:
    print("First Number is Greater then Second Number")
else:
    print("Second number is Greater then First Number")




first_number = input("Plirst Enter First Number: ")
second_number = input("Please Enter Second Number: ")
if first_number > second_number:
    print("First Number is Greater then Second Number")
else:
    print("Second number is Greater then First Number")


first_number = input("Please Enter First Number: ")
second_number = input("Please Second Number: ")
if first_number > second_number:
    print(f"{first_number} is Greater then {second_number}. ")
else:
    print(f"{second_number} is Greater then {first_number}. ")


percentage = int(input("Please enter your percentage"))
grade = " "
if percentage >= 50:
     grade = "you have pass your exam. and your Grade is A "
else:
    grade = "Sorry You are failed and your Grade is F :"
print(grade)




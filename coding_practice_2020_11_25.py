#34

number = int(input("enter an integer: "))

if number % 2 == 1:
    print("number is odd")
else:
    print("number is even")

#36

letter = input("enter a lower case letter ")

if letter == "a" or "e" or "i" or "o" or "u":
    print ("its a vowel")
elif letter == "y":
    print ("only sometimes")
else:
    print("not a vowel")

#37

sides = int("how may sides? ")
if sides == 3:
    name = triangle
if sides == 4:
    name = rectangle
if sides == 5:
    name = pentagon
else:
    print("from 3-5 please")
print(name)

#38

month = input("enter a month")
if month =="january" or "march" or "may" or "july" or "august" or "october" or "december":
    print("31 days")
if month == "feburary":
    print("28 or 29 days")
else:
    print("30 days")

#40

side1 = float(input("length of first side"))
side2 = float(input("length of second side"))
side3 = float(input("length of third side"))

if side1 == side2 == side3:
    print("equilateral")
elif side1 == side2 or side2==side3 or side1 == side3:
    print("iscoles")
else:
    print("scalene")

#44

month = input ("enter a month: ")
day = int(input("enter a day"))

if month == "january" or month == "febuary":
    print("winter")
elif month == "march":
    if day < 20:
        print("winter")
    else:
        print("spring")
elif month == "april" or "may":
    print("spring")
elif month == "june":
    if day < 21:
        print("spring")
    else:
        print("summer")
elif month == "july" or "august":
    print("summer")
elif month == "september":
    if day < 22:
        print("summer")
    else:
        print("autumn")
elif month == "october" or "november":
    print("autumn")
elif month == "december":
    if day < 21:
        print("fall")
    else:
        print("winter")



#46

month = input ("enter a month: ")
day = int(input("enter a day"))

if month == "january" and day == 1:
    print("new year's")
elif month == "july" and day == 1:
    print("canada's day")
elif month == "december" and day == 25:
    print("chirstmas")
else:
    ("no holiday on that day")
#48

year = int(input("enter a year: "))

if year%12==8:
    print("dragon")
elif year%12==9:
    print("snake")
elif year%12==10:
    print("horse")
elif year%12==11:
    print("sheep")
elif year%12==0:
    print("monkey")
elif year%12==1:
    print("rooster")
elif year%12==2:
    print("dog")
elif year%12==3:
    print("boar")
elif year%12==4:
    print("mouse")
elif year%12==5:
    print("ox")
elif year%12==6:
    print("tiger")
elif year%12==7:
    print("rabbit")

#51:

A_plus = 4.0
A = 4.0
A_minus = 3.7
B_plus = 3.3
B = 3.0
B_minus = 2.7
C_plus = 2.3
C = 2.0
C_minus = 1.7
D_plus = 1.3
D = 1.0
F = 0

grade = input("enter in a letter grade eg.(A_minus, A, A_plus)")

if grade == "A_plus" or "A":
    print(A_plus)
elif grade == "A_minus":
    print(A_minus)
elif grade == "B_plus":
    print(B_plus)
elif grade == "B_minus":
    print(B_minus)
elif grade == "B":
    print(B)
elif grade == "C_plus":
    print(C_plus)
elif grade == "C":
    print(C)
elif grade == "C_minus":
    print(C_minus)
elif grade == "D_plus":
    print(D_plus)
elif grade == "D":
    print(D)
elif grade == "F":
    print(F)

#53:
unacceptable = 0
acceptable = 0.4
merit = 0.6

performance = float(input("enter your performance value "))
if performance == unacceptable:
    print("no raise for you")
if performance == acceptable:
    print(f"you get a raise of {2400*0.4} dollars")
if performance >= merit:
    print(f"you get a raise of {2400*performance} dollars")
    
#codingbat #1:
def hello_name(name):
  return "Hello " + name + "!"
  
#2:
def make_abba(a, b):
  return a+2*b+a
#3:
def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"

#4:
def make_out_word(out, word):
  return out[:2] + word + out[2:]

#5:
def extra_end(str):
  return str[-2:]*3
  
#6:
def first_two(str):
  if len(str)<=2:
    return str 
  else:
    return str[:2]
#7:
def first_half(str):
  return str[:len(str)/2]
  
#8:
def without_end(str):
   return str[1:-1]
   
#9:
def combo_string(a, b):
  if len(a)<len(b):
    return a+b+a 
  else:
    return b+a+b
      
#10:

def non_start(a, b):
  return a[1:]+b[1:]

  


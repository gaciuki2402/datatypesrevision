num1=546
num2=345

if num1<num2:
    print(True)
else:
    print(False)


    if num1>num2:
        print(True)
    else:
        print(False)
iwakeupearlyinthemorning=True
if iwakeupearlyinthemorning:
    print('i will attend the meeting')
else:
    print('will just take a shower')

iwilldance=False
if iwilldance:
    print("when you attend the cooncert")

else:
    print("when you dont attend the concert")
online=False
if online:
    print("Green Button")
else:
    print("no green button")



availablity=True
sent1="I was at the lib"
sent2=", before you called."
if availablity: #True
    print(sent1+sent2)
else: #False
    print("I was not at the lib, and you never called")

first_name="Grace"
second_name=" Gaciuki"
full_name=first_name+second_name
print(full_name)
if 25+30==95:
    print("i am a genius!")
else:
    print("i am not a genius")

if False:
    print("the disease will get diagnosed")
else:
    print("the diagnosis of the disease will fail")


isRaining=False
if isRaining:
    print("Wear warm clothes")
else:
    print("wear light clothes")

isNight=True
if isNight:
    print("It's dark: Lights switched on")
else:
    print("It's day time: Lights switched off")

age=19 #true
if age>18: #True
    print("Youth")
else:#False
    print("Teenager")

#baby0-10
#teenager11-18
#Youth 18-35
#adult 35-60
#Old 60>

age=13
if age>0 and age<=10:
    print("Baby")
elif age>=11 and age<18:
    print("Teenager")
elif age>=18 and age<=35:
    print("Youth")
elif age>35 and age<=60:
    print("Adult")
elif age>60:
    print("Old")
else:
    print("Invalid Age")

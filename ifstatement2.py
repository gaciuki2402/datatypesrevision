
num1=456
num2=456
if num1>num2:
    print(True)
else:
    print(False)

    if num1==num2:
        print(True)
    else:
        print(False)

    if num1<num2:
            print(False)
    else:
            print(True)


busy=False
if busy:
    print("am doing my assignment.")
else:
    print("am not doing my assignment.")

iamtired=False
if iamtired:
    print("i will sleep.")
else:
    print("i will watch the show.")

read=False
if read:
    print("bluetick")
else:
    print("greytick")

sick=False
if sick:
    print("Malaria")
else:
    print("just a fever")

day=True
S1="On sunday"
S2=", i will go to church"
S3=" i will not go to church"
if day:
    print(S1+S2)
else:
    print(S3)

grade=67
if grade>0 and grade<=30:
    print("terribly failed")
elif grade>30 and grade<=45:
    print("fail")
elif grade>45 and grade<60:
    print("fair")
elif grade>=60 and grade<=80:
    print("pass")
else:
    print("invalid grade")

#Days of the week

day="SAturday".lower()
if day=="monday":
    print("wash the dishes")
elif day=="tuesday":
    print("tidy the room")
elif day=="wednesday":
    print("attend the meeting")
elif day=="thursday":
    print("wash the clothes")
elif day=="saturday":
    print("go to church")
elif day=="sunday":
    print("visit grandpa")
else:
    print("invalid day")





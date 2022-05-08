islamic=float(input("enter islamic mark: "))
arabic=float(input("enter arabic mark: "))
english=float(input("enter english mark: "))
marks=[0,0,0,0,0,0]
marks[0]=islamic
marks[1]=arabic
marks[2]=english
print("***************************************")
print(''' choose a track from the next menu:
1-enter s to select scientific
2-enter l to select literary
''')
track=input("enter your track: ")
if track=='s':
    physics=float(input("enter physic mark: "))
    chemistry=float(input("enter chemistry mark: "))
    marks[3]=physics
    marks[4]=chemistry
    print(''' if choose 'a' track from the next menu:
    1-enter e to select applied branch
    2-enter b to select biological
    ''')
    print("*******************************")



    track=input("enter your track: ")
    if track=='e':
        math=float(input("enter math mark: "))
        marks[5]=math
        total=sum(marks)

    else:
        biology=float(input("enter biology mark: "))
        marks[5]=biology
        total=sum(marks)

    

else:
    geograph=float(input("enter geograph mark: "))
    history=float(input("enter history mark: "))
    computer=float(input("enter computer mark: "))
    marks[3]=geograph
    marks[4]=history
    marks[5]=computer

total=sum(marks)
avg=total/6
print("the total is: ",total)
print("the average is : ",avg)
    
if avg>=90:
    print("the grade is (A)")

elif avg>=80:
    print("the grade is (B)")

elif avg>=70:
    print("the grade is (C)")

elif avg>=60:
    print("the grade is (L)")

else:
    print("result is (fail)")
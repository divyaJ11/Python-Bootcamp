#Zodiac project
#add new features
next = True
while next==True :
    print('''
1. Aries
2. Taurus
3. Gemini
4. Cancer
5. Leo
6. Virgo
7. Libra
8. Scorpio
9. Sagittarius
10. Capricorn
11. Aquarius
12. Pisces
    ''')

    n=int(input("Pick your sign number and press enter  "))

    if n==1:
        print("Aries")
    elif n==2:
        print("Taurus")
    elif n==3:
        print("Taurus")
    elif n==4:
        print("Taurus")
    elif n==5:
        print("Taurus")
    elif n==6:
        print("Taurus")
    elif n==7:
        print("Taurus")
    elif n==8:
        print("Taurus")
    elif n==9:
        print("Taurus")
    elif n==10:
        print("Taurus")
    elif n==11:
        print("Taurus")
    elif n==12:
        print("Pisces")
    else:
        print("Are you sure about this number?")

    '''temp = input("Do you want to continue Y/N   ")
    if temp == "Y":
        next =True
    else:
        next =False'''
    #one liner for if else
    next = True if input("Do you want to continue Y/N   ") =="Y" else False
print("Thank You")




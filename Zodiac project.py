#Python bootcamp - Zodiac project


next = True     #counter variable 

#loop to print the zodiac signs
while next==True :
    print('''
-----------------------------------Zodiac Signs-------------------------------------
1. Aries (Mar 21 – Apr 20)
2. Taurus (Apr 21 – May 21)
3. Gemini (May 22 – June 21)
4. Cancer (June 22 – July 22)
5. Leo (July 23 – Aug 23)
6. Virgo (Aug 24 – Sept 22)
7. Libra (Sept 23 – Oct 23)
8. Scorpio (Oct 24 – Nov 22)
9. Sagittarius (Nov 23 – Dec 21)
10. Capricorn (Dec 22 – Jan 20)
11. Aquarius (Jan 21 – Feb 18)
12. Pisces (Feb 19 – Mar 20)
    ''')

    valid = False   #flag variable for validation
    
    #loop continues to run till valid input is given
    while not valid:
        try:
            #Accept the sign number
            n = int(input("\nPick your sign number and press enter  ")) 

            #If entered value is in the permissible range 'valid' is set to True
            valid = True if n in range(1,13) else False
            if not valid:
                print("\n!! Number entered is out of the permissible range  !!") 

        except:
            #error message for invalid data type
            print("\n!! Enter valid numeric value   !!")

    if n==1:
        print("Aries:")
        print("Success if you're involved with the media. Here's a golden chance to showcase your talent, as all eyes are on you. Your skills and talent will be acknowledged, and short-term goals will see fulfillment.")
    elif n==2:
        print("Taurus:")
        print("Today may be the beginning of an exciting relationship. You will feel oneness with words and actions, communicating with your colleagues with ease. The spot light at whichever party you go to will be following you as you will storm the place with your enthusiasm and charisma.")
    elif n==3:
        print("Gemini:")
        print("Your interest and performance in sports will go from strength to strength. You are feeling a bit anxious and will not be able to concentrate on a single job. Instead, you will move from one project to another. You will spend more time at work and less time with the family.")
    elif n==4:
        print("Cancer:")
        print("Enough of waiting on the sidelines, watching others take credit for all your hard work. Today, you will stake your claim to what is rightfully yours, the due credit for your work. Surprisingly for you, your peers and superiors will not only appreciate your work without any fuss, but also share with you the big plans they have in store for you.")
    elif n==5:
        print("Leo:")
        print("Today, you will be gripped by the desire to shop till you drop, even if it means having to spend a small fortune from your hard-earned savings! You have no problem with that, especially if all the money-spending is being undertaken to please your sweetheart. Those who try to warn you against carrying out your plans will be doing so in vain. It's not for nothing they say, 'Love is blind.'")
    elif n==6:
        print("Virgo:")
        print("All you have to do is start what you intend to do, and its success will automatically fall in. Such is the day today for you. Financial transactions will be rewarding. However, the day may not be as exciting as you expect. But then again, don't expect – just go with the flow.")
    elif n==7:
        print("Libra:")
        print("You are at your best when communicating with others, and your silver-tongued speech will charm many. Your day will be spent in negotiating, meetings, and in interacting with people to get things done. At work, you may be put in charge of some investigative task. Towards the evening, people around you will find you incredibly charming and irresistible.")
    elif n==8:
        print("Scorpio:")
        print("Take the lonely road today in business ventures. Professionally, you are capable of managing massive missions. Be set to administer your department all by yourself. You shall stake a claim as a great team leader today.")
    elif n==9:
        print("Sagittarius:")
        print("Belligerent – this word describes your state today. Good news, long since awaited, will come by at the workplace. Imagination is set to fly sky-high as you while the evening away in the pleasant company of someone from the opposite sex.")
    elif n==10:
        print("Capricorn:")
        print("It is time again for that once-in-blue-moon mood swing. You will be easily irked by everyday activities and may let small, less important things bother you too much. But the darkest hour is just before dawn. Things should start looking up later in the day. You enjoy doing things others won't dare, and for all you know, you may have already won millions of hearts with your impressive personality.")
    elif n==11:
        print("Aquarius:")
        print("Worried about your future? Just approach your work more seriously. You may be overburdening yourself by helping others. While this is noble, it shouldn't be at the cost of your own health. By noon, your spirits will lift. You realise that it's okay to be a little selfish.")
    else:
        print("Pisces:")
        print("It is a good day for you, since all the projects you take up today will reach a satisfactory conclusion. However, this does not mean that you will not be strung out, a fact you would do well to keep hidden, lest your competitors try to take advantage of it.")
    

    
    #'next' is set to True if user wants to continue
    next = True if input("\nDo you want to continue Y/N   ") =="Y" else False
print("""-----------------------------------Thank You-------------------------------------""")




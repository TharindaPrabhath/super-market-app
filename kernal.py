print('''  Welcome my dear! Ther is no place better than this.
                       -USER GUIDE-
           y- yes
           n- no
           1- pay via bank card
           if you want to pay via cash, please be kind enough to enter any number except 1
        If you have any problems nothing to do ''')
print("-----------------------------------------------------------------------------------------")
#to build a good looking interface

no_of_items = int(input("How many items: "))
#conting the number of different items in the given paper

count=0
total=0

while count<no_of_items :
    count=count+1
    try:
        inpt_1=int(input("Unit Price: Rs."))
    except ValueError:
        print("No letters can be included for unit price")
    try:
        inpt_2=int(input("Number of units: "))
    except ValueError:
         print("No letters can be included for number of units")
    total=total+inpt_1*inpt_2

print("RS.",total)

inpt_3=int(input("How do you wish to pay? "))

if inpt_3==1:
    inpt_4=input("Please enter the bank name of the card: ")
        
    isEight=False
    while isEight==False:
        inpt_5=(input("Enter the card number: "))
        if  len(inpt_5)==8:
            print("Thank you for your payment")
            break
        else:
            print("Invalid Number!")
#Counting the digits of the entered 'card number'.
#It should be 8 
      
else:
    print("You can pay by cash")
    
inpt_6=input("Do you want a bill? (y/n) ")

if inpt_6=="y":
    inpt_7=input("Enter your name: " )
    print(''' Hello ''' +inpt_7 + "!"
          
          ''' You have paid via your ''' +inpt_4+ ''' card
              Your total price is,Rs.''' ,total)
    
elif inpt_6=="n":
    print(" Ok then")
    print(" Have a nice day!")
else:
    print('''Seems like you have entered a invalid input
            Please see the user guide given below
            
                        -USER GUIDE-
           y- yes
           n- no
           1- pay via bank card
           if you want to pay via cash, please be kind enough to enter any number except 1''')

inpt=input("     ..................................................................     ")
#the reason for use this 'inpt' is for display the final result 
#in the terminal without cancelling 
# in miliseconds. 
     
           

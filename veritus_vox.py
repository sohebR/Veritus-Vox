import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning !!")
        print("Good Morning !!")
    elif hour >=12 and hour < 17:
        speak("Good Afternoon!")
        print("Good Afternoon !!")
    else :
        speak("Good Evening!!")
        print("Good Evening!!")

if __name__ == '__main__':
    print("\n\n\n")
    wishMe()
    speak("WELCOME TO VERITUS VOX")
    print("\nWELCOME TO VERITUS VOX")
    speak("These are the items that are available today:")
    print("\nThese are the items that are available today:")
    total_cost = 0
    purchased_items = []
    
    grocery_items = {
        'Sugar': 20.0,
        'Salt': 10.0,
        'Milk': 27.0,
        'Bread': 25.5,
        'Eggs': 5.8,
        'Biscuit':10.0,
                    }
    for a in grocery_items.keys():
        speak(a)
        print(f"-{a}")


    while True:
        user_input1 = speak("Enter the item you want to buy (or 'done' to finish): ")
        user_input = input("\nEnter the item you want to buy (or 'done' to finish): ").capitalize()
        if user_input == 'Done':
            break
        elif user_input in grocery_items: 
            if(user_input=='Biscuit'):
                speak(f"Enter quantity of {user_input} in packets: ")
                quantity = int(input(f"\nEnter quantity of {user_input} in pkts: "))
                quantity_f=str(quantity)+str(" pkt")
                item_cost = grocery_items[user_input] * quantity
                total_cost += item_cost
                purchased_items.append((user_input, quantity_f, item_cost))
            elif(user_input=='Milk'):
                speak(f"Enter quantity of {user_input} in litres: ")
                quantity = float(input(f"\nEnter quantity of {user_input} in lit: "))
                quantity_f=str(quantity)+str(" ltr")
                item_cost = grocery_items[user_input] * quantity
                total_cost += item_cost
                purchased_items.append((user_input, quantity_f, item_cost))
            elif(user_input=='Bread'):
                speak(f"Enter quantity of {user_input} in packets: ")
                quantity = int(input(f"\nEnter quantity of {user_input} in pkts: "))
                quantity_f=str(quantity)+str(" pkt")
                item_cost = grocery_items[user_input] * quantity
                total_cost += item_cost
                purchased_items.append((user_input, quantity_f, item_cost))
            elif(user_input=='Eggs'):
                speak(f"Enter quantity of {user_input} in pieces: ")
                quantity = int(input(f"\nEnter quantity of {user_input} in pcs: "))
                quantity_f=str(quantity)+str(" pcs")
                item_cost = grocery_items[user_input] * quantity
                total_cost += item_cost
                purchased_items.append((user_input, quantity_f, item_cost))
            else:
                speak(f"Enter quantity of {user_input} in kilograms: ")
                quantity = float(input(f"\nEnter quantity of {user_input} in kgs: "))
                quantity_f=str(quantity)+str(" kgs")
                item_cost = grocery_items[user_input] * quantity
                total_cost += item_cost
                purchased_items.append((user_input, quantity_f, item_cost))
            
                
        else:
            speak("Invalid item. Please choose a valid item or type 'done' to finish.")
            print("\nInvalid item. Please choose a valid item or type 'done' to finish.\n")

    speak("Enter the name of the Customer:")      
    name=input("\nEnter the name of the Customer:\n")
    speak("Do you want to enter your phone number? Type 'y' for Yes or 'n' for No")
    p = input("Do you want to enter your phone number? Type 'y' for Yes or 'n' for No :\n").capitalize()
    if p == 'Y':
        ph=input("Enter the phone number of the customer:\n")
        print("\n\nMobile Number:",ph)
        speak("Here is your receipt")
        print("\n******************** Grocery Bill********************")
        print("Name of Customer:",name)
    else :
        speak("Here is your receipt")
        print("\n\n******************** Grocery Bill********************")
        print("Name of Customer:",name)
    print("Item\t\tQuantity\tPrice\t\tTotal")
    print("---------------------------------------------------------")
    for item, quantity_f, item_cost in purchased_items:
        print(f"{item}\t\t{quantity_f}\t\t{grocery_items[item]:.2f}\t\t{item_cost:.2f}")
    print("---------------------------------------------------------")
    print(f"Total\t\t\t\t\t\tRs.{total_cost:.2f}")
    print("*********************************************************")

    speak("Are you going to pay with Cash or Credit card ?")
    speak("If paying with cash then enter 'cash' and if with credit card then enter 'card'")
    pay = input("\nIf paying with cash then enter 'cash' and if with credit card then enter 'card':\n")
    if pay=="cash":
        speak("Thank you for the payment ! I hope you have a nice day.")
        print("\n\nThank you for the payment ! I hope you have a nice day.")
    else :
        def every_other_digit(credit_card):
            sum = 0
            isAlternateDigit = False
            while credit_card > 0:
                if isAlternateDigit:
                    last_digit = credit_card % 10
                    product = multiplyAndSum(last_digit)
                    sum += product
                else:
                    last_digit = credit_card % 10
                    sum += last_digit
                isAlternateDigit = not isAlternateDigit
                credit_card //= 10
            return sum

        def multiplyAndSum(last_digit):
            multiply = last_digit * 2
            sum = 0
            while multiply > 0:
                last_digit_multiply = multiply % 10
                sum += last_digit_multiply
                multiply //= 10
            return sum

        def number(credit_card):
            count = 0
            while credit_card > 0:
                count += 1
                credit_card //= 10
            return count

        def isValidAmex(credit_card, dig):
            first_two = credit_card // pow(10, 13)
            return (dig == 15) and (first_two == 34 or first_two == 37)

        def isValidMaster(credit_card, dig):
            first_one = credit_card // pow(10, 15)
            return (dig == 16) and (first_one ==5 )

        def isValidVisa(credit_card, dig):
            if dig == 13:
                first_one = credit_card // pow(10, 12)
                return first_one == 4
            elif dig == 16:
                first_one = credit_card // pow(10, 15)
                return first_one == 4
            return False

        speak("\nPlease enter your credit card number")
        credit_card = int(input("Credit card : "))
        sum_every_other_digit = every_other_digit(credit_card)
        dig = number(credit_card)
        amex = isValidAmex(credit_card, dig)
        master = isValidMaster(credit_card, dig)
        visa = isValidVisa(credit_card, dig)

        if sum_every_other_digit % 10 != 0:
            speak("Sorry! The card is invalid.")
            print("\nThe card is invalid !!")
            speak("Please pay via cash and thank you for coming!!")
            print("\nPlease pay via cash and thank you for coming!!")
        else:
            if amex:
                speak("This card is an valid American Express credit card. ")
                print("\nAmerican Express credit card")
            elif master:
                speak("This card is an valid Mastercard credit card")
                print("\nMastercard")
            elif visa:
                speak("This card is an valid Visa credit card")
                print("\nVisa Credit card")
            else:
                speak("This is a valid credit card.")
                print("\nValid credit card")
        speak("Thank you for the payment!!! Have a nice day!!")
        print("\nThank you for the payment!!! Have a nice day!!")
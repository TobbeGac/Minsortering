import random
import Sortmodule

looping = True
listnumbers = []

for tnum in range(5):
    tslumptal = random.randint(0, 100)
    listnumbers.append(tslumptal)
    print(tslumptal)

while looping:

    val = Sortmodule.create_menu()

    if (val == "1"):
        print("\nSkriver ut lista med slump---------------------")
        
        
        Sortmodule.print_list_numbers(listnumbers)
        nysorterade_listnumbers = Sortmodule.bubble_sort(listnumbers)
        print("SORTERAR")
        Sortmodule.print_list_numbers(nysorterade_listnumbers)
        fortsatt = input("\nVill du fortsätta? j/n ")
        if(fortsatt == "n"):
            break

    elif (val == "2"):
        print("\n-Skriver listnumbers med slumptal-----------------------------")
        listnumbers2 = listnumbers
        Sortmodule.print_list_numbers(listnumbers)
        print("\n-Sortera med python-----------------------")
        listnumbers2.sort()
        Sortmodule.print_list_numbers(listnumbers2)

        fortsatt = input("\nVill du fortsätta? j/n ")
        if(fortsatt == "n"):
            break
 
    else:
        break
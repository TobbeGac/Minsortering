def bubble_sort(tset): 
    tlist = tset.copy()
    langd = len(list)
    bytplats = False

    for i in range(langd-1):

        for j in range(0, langd-1):
            
            if( tlist[j] > tlist[j+1]):
                bytplats = True
                tlist[j], tlist[j + 1] = tlist[j + 1], tlist[j]

        if not bytplats:
            return
        
    return tlist

def print_list_numbers(tlist):
    string_nr = " ".join(str(num) for num in tlist)
    print(string_nr)
    

def create_menu():
    print("\n----:MENY SORTERINGS TEST---------------------\n")
    print("1. Använd min egen gjorda BubbleSort")
    print("2. Använd Pythons sort() funktion")
    print("3. Avsluta programmet\n")

    val = input("\n Mata in val: ")

    return val
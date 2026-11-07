import json
import requests 




tries = 5


WOTD = "BLANK" 

fly = input("Enter Try: ")

while tries !=0:
    
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{fly}"


    session = requests.Session()


    response = session.get(url)

    if response.status_code == 200:
         
        for i in range(len(fly)): 
            if fly[i] == WOTD[i]: print(fly[i]," Green!")
            elif fly[i] in WOTD: print(fly[i], " Orange..")
            else: print(fly[i], " NO")
        
        if fly != WOTD:
            tries -= 1
            print(tries,"try(ies) remaining")
            fly = input("Entry Try: ")
        elif fly == WOTD:
            print("Congrats I guess..you solved it...")
            tries = 0
    else:
        print("Word does not exist...try again..")
        fly = input("Enter Try: ")
        continue









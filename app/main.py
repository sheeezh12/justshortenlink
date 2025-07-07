import json
import os

def write(origin, shorten):
    with open("db/db.json", "r") as file:
        data = json.load(file)

    if origin in data.values():
        print("data sudah ada")
    else :    
        data[shorten] = origin
        with open("db/db.json", "w") as file:
            json.dump(data, file, indent=4)    
            print("UDAH REK")      

    


write("internetcafe.com", "anakmodnyet")  

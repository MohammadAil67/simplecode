#first edit with commit 
import sys
import clipboard
import json
from pprint import PrettyPrinter

printer = PrettyPrinter()

key_json = 'key.json'
link_json = 'Linky.json'
Koddo_json = 'Coded.json'


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)


def load_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
        return data

def ArrayFile():
    arraytxt = 'array.txt'
    with open(arraytxt, 'r') as f:
        array = f.readline().strip()
        array2 = f.readline().strip()
        
        return array, array2
    
filearray, filearray2 = ArrayFile() 


if len(sys.argv) == 2:
    command = sys.argv[1]
    lik = clipboard.paste()
    save_json = key_json
 
    if lik.startswith("https://") or lik.startswith("http://"):
        save_json = link_json
    
    
    for i, j in zip(filearray, filearray2):
        if lik.startswith(i) or lik.find(j) != -1:
            save_json = Koddo_json
            break
   
    data = load_json(save_json)

    if command == "save":
        key = input("input the key ")
        data[key] = clipboard.paste()
        save_data(save_json,data)

    elif command == 'load':
        Type = input("is it a code, link or a random statement ")

        if Type == 'code':
            save_json = Koddo_json
        elif Type == 'link':
            save_json = link_json
        else:
            save_json = key_json

        data = load_json(save_json)
        key = input("input the key ")
        if key in data:
             clipboard.copy(data[key])       
        else:
            print("key does not exist") 
    
    elif command == 'list':

        f = load_json(key_json)
        printer.pprint(f)
        f = load_json(link_json)
        printer.pprint(f)
        f = load_json(Koddo_json)
        printer.pprint(f)
         
    elif command == 'delete':
        deletefrom = input("from where do you want to delete ")
        if deletefrom == 'key':
            save_json = key_json
        elif deletefrom == 'link':
            save_json = link_json
        elif deletefrom == "code":
            save_json = Koddo_json
        data = load_json(save_json)
        key = input("input the key ")
        if str(key) in data:
            del  data[key]
            save_data(save_json,data)

    elif command == "readjust":
        save_json = 'key.json'
        dataS = load_json(save_json)
        dataL = load_json(link_json)
        for i in dataS:
            new = dataS.get(i)
            if new.startswith("https:// ") or new.startswith('http:// '):
                #newdata = {}
                #newdata[i] = new
                dataL[i] = new
                save_data(link_json, dataL)
                del dataS[i]
                save_data(save_json, dataS)


else:
    print("unknown command") 


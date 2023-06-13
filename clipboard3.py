
import clipboard
from clipboard2 import save_data
from clipboard2 import load_json

save_json = "key.json"
link_json = 'linky.json'
code_json = 'Coded.json'
breakCond = True
while breakCond:
    
    key = input("give a key to save with ")
    where = input("which file do you want to save in ")
    if where == 'key':
        use_json = save_json
    if where == 'link':
        use_json = link_json
    if where == 'code':
        use_json = code_json

    data = load_json(use_json)
    data[key] = clipboard.paste()
    save_data(use_json,data)

    print("are you done inputting or do you want to enter more data? (y/n)")
    response = input()
    if response.lower() == 'y':
        breakCond = False







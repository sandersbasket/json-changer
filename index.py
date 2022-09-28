import json

def create_json():
    data = {
        "accounts": {
            
        }
    }
    json_string = json.dumps(data, indent = 4)
    with open("config.json", 'w') as file:
        file.write(json_string)

def write_json(new_data, filename='config.json'):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data['accounts'].update(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
 

if __name__ == "__main__":
    create_json()
    accounts = open("accountslist.txt", "r").read().splitlines()
    count = input('How many accounts do you want to record? Max count: {}\n'.format(len(accounts)))
    for line in accounts:
        index = accounts.index(line)
        if index < int(count):
            line = line.split(':')
            new_data = {
                index + 1: {
                    'details': {
                        "username": line[0],
                        "password": line[1]
                    }, 
                    'settings': {
                        "title": [ "I in the game" ],
                        "games": [ 730, 740 ]
                    }
                },
            }
            write_json(new_data)
            print('Login {} | Password: {} | Index: {} succes write in JSON-file'.format(line[0], line[1], index + 1))
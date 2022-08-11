import json

with open('data.json') as json_file:
    data = json.load(json_file)

    # Print the type of data variable
    print("Type:", type(data))

    # Print the data of dictionary
    print("\nclouds:", data['clouds'])

    # for printing the key-value pair of
    # nested dictionary for loop can be used
    print("\nPrinting nested dictionary as a key-value pair\n")
    for i in data['clouds']:
        print("Name:", i['name'])
        print("File Location:", i['xml'])
        print("File Location:", i['csv'])
        print()

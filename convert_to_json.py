import json
with open('.env', 'r') as f:
    envList = f.readlines()
my_dict = {}
my_list=[]
# Loop through each item in the list
for item in envList:
    item2 = item.split('=', 1)
    # Split the item into key and value using the '=' separator
    key, value = item2[0], item2[1].replace('\n','')
    # Add the key-value pair to the dictionary
    my_dict[key] = value

# Loop through each key-value pair in the dictionary
for key, value in my_dict.items():
    # Create a new dictionary with the required keys and values
    new_dict = {"name": key, "value": value}
    my_list.append(new_dict)

# Convert the list to a JSON object
json_obj = json.dumps(my_list, indent=2)

with open('env.json', 'w') as f:
    f.write(json_obj)
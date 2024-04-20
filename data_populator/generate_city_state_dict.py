from city_state_list import cities_and_states

state_city_dict = dict()

for item in cities_and_states:
    state = item["state"]
    city = item["city"]
    if not state in state_city_dict:
        state_city_dict[state] = []
        
    if not city in state_city_dict[state]:
        state_city_dict[state].append(city)

dict_string = "state_cities = {"
for key in state_city_dict.keys():
    dict_string += "\n\""
    dict_string += key + "\": [\n"
    for item in state_city_dict[key]:
        dict_string +=  "   \"" + item + "\",\n"
    dict_string += "],"
dict_string += "}"
    

with open("city_state_dict.py","w+") as file:
    file.write(dict_string)
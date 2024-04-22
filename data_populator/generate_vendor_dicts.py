from random import seed, randint, uniform
from city_state_dict import state_cities

RNG_SEED = 0
STREET_NUM_MAX = 3000

vendor_names = ["Walmart", "Target", "Family Dollar", "Stop & Shop"]

included_states = ["Rhode Island"]

def generate_vendors():
    
    seed(RNG_SEED)
    
    result = [[],[]]
    
    city_id = 1
    vendor_id = 1
    for state in included_states:
        for city in state_cities[state]:
            result[1].append({
                "city_id":city_id,
                "city":city,
                "state":state
                              })
            for vendor in vendor_names:
                street_num = randint(1, STREET_NUM_MAX)
                street_name = city
                if randint(0,1):
                    street_name += " Ave"
                else:
                    street_name += " St"
                
                result[0].append({
                    "vendor_id": vendor_id,
                    "vendor": vendor,
                    "street_num": street_num,
                    "street_name": street_name,
                    "city_id": city_id
                    
                })
                vendor_id += 1
            city_id += 1
    
    return result

if __name__ == "__main__":
    print(generate_vendors())
            
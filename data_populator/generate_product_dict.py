from foundationDownload import foods
from random import uniform, seed

SEED = 0

def generate_foods():
    
    seed(SEED)
    LOWER_PRICE = 3
    UPPER_PRICE = 7
    
    result = dict()

    for item in foods["FoundationFoods"]:
        if "foodPortions" in item and len(item["foodPortions"]) > 0:
            key = item["description"]
            result[key] = dict()
            result[key]["serving_size"] = item["foodPortions"][0]["gramWeight"]
            result[key]["price"] = round(uniform(LOWER_PRICE,UPPER_PRICE),2)
        
    return result

if __name__ == "__main__":
    print(generate_foods())
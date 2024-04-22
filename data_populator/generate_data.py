from generate_product_dict import generate_foods
from generate_vendor_dicts import generate_vendors
from my_datatime import DateTime, DateTimeGenerator
from random import seed, randint, uniform

dt_gen = DateTimeGenerator()
RNG_SEED = 0
STREET_NUM_MAX = 3000

monthly_inlfation = 0.003

package_servings = [1,4,6,8,12]
package_markups = [
    0,
    1,
    0,
    0,
    0.9,
    0,
    0.85,
    0,
    0.8,
    0,
    0,
    0,
    0.75
    ]

brands = ["Brand A",
          "Brand B",
          "Brand C"]
brand_count = len(brands)

vendors, cities = generate_vendors()

brand_markups = [0.8,1.0,1.2]
BRAND_DEVIATION_LOWER = 0.7
BRAND_DEVIATION_UPPER = 1.3
VENDOR_DEVIATION_LOWER = 0.85
VENDOR_DEVIATION_UPPER = 1.15
AMOUNT_DEVIATION_LOWER = 0.9
AMOUNT_DEVIATION_UPPER = 1.1

foods = generate_foods()

vendor_names = ["Walmart", "Target", "Family Dollar", "Stop & Shop"]

vendor_markups = {"Walmart": 1.2,
                  "Target": 1.3,
                  "Family Dollar": 1,
                  "Stop & Shop": 1.4}

def generate_products ():
    product_entries = []
    for food in foods.keys():
        for brand in range(brand_count):
            if randint(1,5) < 5:
                product_entries.append([food, brand])
    
    return product_entries

def generate_items_and_stocks():
    seed(RNG_SEED)
    products = generate_products()
    prices = []
    quantities = []
    price_id = 1
    quantity_id = 1
    items = []
    item_id = 1
    stocks = []
    for v in vendors:
        v_dev = uniform(VENDOR_DEVIATION_LOWER, VENDOR_DEVIATION_UPPER)
        stock = []
        for p_id, p in enumerate(products):
            if randint(1,5) < 4:
                b_dev = uniform(BRAND_DEVIATION_LOWER, BRAND_DEVIATION_UPPER)
                for pack_size in package_servings:
                    if pack_size == 1 or randint(1,5) < 4:
                        pack_markup = package_markups[pack_size]
                        quantities.append(
                            [round(foods[p[0]]["serving_size"]*uniform(
                                AMOUNT_DEVIATION_LOWER,
                                AMOUNT_DEVIATION_UPPER
                                ),2),
                            "grams",
                            pack_size
                                            ])
                        quantity_id += 1
                        highest_date = 0
                        highest_index = 0
                        for _ in range(randint(3,7)):
                            dt = dt_gen.generate_datetime_int()
                            if dt > highest_date:
                                highest_date = dt
                                highest_index = len(stock) - 1
                            inflation = 1 + ((dt >> 18) - (dt_gen.min_year << 3))*monthly_inlfation
                            price = foods[p[0]]["price"]
                            
                            price *= vendor_markups[v["vendor"]]
                            price *= brand_markups[p[1]]
                            price *= b_dev
                            price *= v_dev
                            price *= inflation
                            price *= pack_size
                            prices.append([round(price,2), DateTime.int_to_sql(dt)])
                            
                            
                            items.append(
                                [
                                    p_id,
                                    quantity_id,
                                    price_id
                                ]
                            )
                            stock.append([item_id,0])
                            item_id += 1
                            price_id += 1
                            
                        stock[highest_index][1] = 1
                        highest_date = 0
                        highest_index = 0
        
        stocks.append(stock)
                        
    result = {
        "price" : prices,
        "quantity": quantities,
        "item": items,
        "stock": stocks,
        "product": products
    } 
    
    for p in result["product"]:
        p[1] = brands[p[1]]
        
    return result
                    
def package_all_data():
    result = generate_items_and_stocks()
    result["vendor"] = vendors
    result["city"] =  cities
    
    return result
    ...

if __name__ == "__main__":
    result = package_all_data()
    a = 1
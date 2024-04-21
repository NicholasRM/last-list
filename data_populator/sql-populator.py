import mysql.connector
from random import seed, randint, uniform
from city_state_dict import state_cities
from generate_product_dict import generate_foods
from data_populator.generate_vendor_dicts import generate_vendors

CNX = mysql.connector.connect(user='root', password='password123',
                              host='localhost',
                              database='LastList',
                              use_pure=False)

RNG_SEED = 0
STREET_NUM_MAX = 3000

monthly_inlfation = 0.003

package_servings = [1,4,6,8,12]
package_markups = [1,0.9,0.8,0.7]

brands = ["Brand A",
          "Brand B",
          "Brand C",
          "Brand D",
          "Brand E"]

vendors, cities = generate_vendors()

brand_markups = [0.8,0.9,1.0,1.1,1.2]
BRAND_DEVIATION_LOWER = 0.7
BRAND_DEVIATION_UPPER = 1.3

products = generate_foods()

vendor_names = ["Walmart", "Costco Wholesale", "Target", "Family Dollar", "Stop & Shop"]

vendor_markups = {"Walmart": 1.3,
                  "Costco Wholesale": 1.2,
                  "Target": 1.2,
                  "Family Dollar": 1,
                  "Stop & Shop": 1.4}

max_item_id = 0

def populate_vendor_and_city():
    if CNX and CNX.is_connected():
        with CNX.cursor() as cursor:
            for c in cities:
                city_id = c["city_id"]
                city = c["city"]
                state = c["state"]
                result = cursor.execute(f"""
                            INSERT INTO city(city_id, city, state) VALUES
                            ('{city_id}', '{city}','{state}');
                        """)
            for v in vendors:
                vendor_id = v["vendor_id"]   
                vendor = v["vendor"]
                street_num = v["street_num"]
                street_name = v["street_name"]
                city_id = v["city_id"]
                
                result = cursor.execute(f"""
                            INSERT INTO vendor(vendor_id, name, street_number, street_name, city_id) VALUES
                            ({vendor_id}, '{vendor}', {street_num}, '{street_name}', {city_id});
                        """)

def clear_tables():
    print("Attempting to clear tables related to item")
    if CNX and CNX.is_connected():
        with CNX.cursor() as cursor:
            print("Clearing contains")
            result = cursor.execute("TRUNCATE TABLE contains")
            print("Clearing stock")
            result = cursor.execute("TRUNCATE TABLE stock")
            print("Clearing item")
            result = cursor.execute("TRUNCATE TABLE item")
            print("Clearing product_rating")
            result = cursor.execute("TRUNCATE TABLE product_rating")
            print("Clearing vendor_rating")
            result = cursor.execute("TRUNCATE TABLE vendor_rating")
            print("Clearing product")
            result = cursor.execute("TRUNCATE TABLE product")
            print("Clearing price")
            result = cursor.execute("TRUNCATE TABLE price")
            print("Clearing quantity")
            result = cursor.execute("TRUNCATE TABLE quantity")
            print("Clearing vendor")
            result = cursor.execute("TRUNCATE TABLE vendor")
            print("Clearing city")
            result = cursor.execute("TRUNCATE TABLE city")
    
    print("All important tables have been cleared")

def main():
    global CNX
    response = input("""
             Would you like to use defualt settings?:
             username: root
             password: password123
             host: localhost
             database: LastList
             
             (y/n):
             """)
    if response != "y" or response != "Y":
        db_name = input("Enter name of LastList database:\n")
        db_host = input("Enter host:\n")
        db_user = input("Enter username:\n")
        db_password = input("Enter password:\n")
    else:
        mysql.connector.connect(user='root', password='password123',
                              host='localhost',
                              database='LastList',
                              use_pure=False)
        
    try:
        CNX = mysql.connector.connect(user=db_user, password=db_password,
                              host=db_host,
                              database=db_name,
                              use_pure=False)
        print("Connection successful.")
        response = input(
"""
!!!WARNING!!!:
This script will clear all existing data pertaining to
the item table of the LastList database in order to
ensure items are generated properly.
The affected tables include (in order of deletion):
contains
stock
item
product_rating
vendor_rating
product
price
quantity
vendor
city


Proceed?(y/n):""")
        if response == "y" or response == "Y":
            clear_tables()
            
        
    except:
        print("An error occured while trying to establish MySQL connection")
        
    seed(RNG_SEED)
    
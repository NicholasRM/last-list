import mysql.connector
import random
from city_state_dict import state_cities
cnx = mysql.connector.connect(user='root', password='password123',
                              host='localhost',
                              database='LastList',
                              use_pure=False)

RNG_SEED = 0
STREET_NUM_MAX = 3000
products = ["Coca-Cola"]

product_units = {"Coca-Cola" : "fluid ounces"}

units_per_container = {"Coca-Cola": [12,24]}

containers_per_pack = {"Coca-Cola": [6,12,18]}

base_unit_prices = {"Coca-Cola" : 0.05}

vendor_names = ["Walmart", "Costco Wholesale", "Target", "Family Dollar", "Stop & Shop"]

vendor_markups = {"Walmart": 1.3,
                  "Costco Wholesale": 1.2,
                  "Target": 1.2,
                  "Family Dollar": 1,
                  "Stop & Shop": 1.4}

def generate_vendors():
    for state in state_cities.keys():
        for city in state_cities[state]:
            
            ...
    ...

def generate_item_query(product, price_deviation, vendor, date):
    price = base_unit_prices[product]
    price *= units_per_container[random.randint(0, len(units_per_container) - 1)]
    price *= containers_per_pack[random.randint(0, len(containers_per_pack) - 1)]
    price *= vendor_markups[vendor]
    price *= price_deviation
    price = round(price,2)
    ...

def clear_tables():
    print("Attempting to clear tables related to item")
    if cnx and cnx.is_connected():
        with cnx.cursor() as cursor:
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
    global cnx
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
        cnx = mysql.connector.connect(user=db_user, password=db_password,
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
        
    random.seed(RNG_SEED)
    
import mysql.connector
from generate_data import package_all_data

CNX = None

def populate_vendor_and_city(cities, vendors):
    if CNX and CNX.is_connected():
        with CNX.cursor() as cursor:
            print("Populating city")
            for c in cities:
                city_id = c["city_id"]
                city = c["city"]
                state = c["state"]
                result = cursor.execute(f"""
                            INSERT INTO city(city_id, city, state) VALUES
                            ('{city_id}', '{city}','{state}');
                        """)
            print("Populating vendor")
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

def populate_product(products):
    print("Populating product")
    if CNX and CNX.is_connected():
        with CNX.cursor() as cursor:
            for p_id, p in enumerate(products):
                result = cursor.execute(f"""
                            INSERT INTO product(product_id, name, brand) VALUES
                            ({p_id + 1}, '{p[0]}', '{p[1]}');
                        """)

def populate_price(prices):
    print("Populating price")
    if CNX and CNX.is_connected():
        with CNX.cursor() as cursor:
            for p_id, p in enumerate(prices):
                result = cursor.execute(f"""
                            INSERT INTO price(price_id, price, date_recorded) VALUES
                            ({p_id + 1}, {p[0]}, '{p[1]}');
                        """)
                
def populate_quantity(quantities):
    print("Populating quantity")
    if CNX and CNX.is_connected():
        with CNX.cursor() as cursor:
            for q_id, q in enumerate(quantities):
                result = cursor.execute(f"""
                            INSERT INTO quantity(quantity_id, measurement, unit, count) VALUES
                            ({q_id + 1}, {q[0]}, '{q[1]}', {q[2]});
                        """)
                
def populate_item(items):
    print("Populating item")
    if CNX and CNX.is_connected():
            with CNX.cursor() as cursor:
                for i_id, i in enumerate(items):
                    result = cursor.execute(f"""
                                INSERT INTO item(item_id, product_id, quantity_id, price_id) VALUES
                                ({i_id + 1}, {i[0]}, {i[1]}, {i[2]});
                            """)
                    
def populate_stock(stocks):
    print("Populating stock")
    if CNX and CNX.is_connected():
            with CNX.cursor() as cursor:
                for v_id, stock in enumerate(stocks):
                    for item in stock:
                        result = cursor.execute(f"""
                                    INSERT INTO stock(vendor_id, item_id, status) VALUES
                                    ({v_id + 1}, {item[0]}, {item[1]});
                                """)
def clear_tables():
    print("Attempting to clear tables related to item")
    if CNX and CNX.is_connected():
        with CNX.cursor() as cursor:
            print("Clearing contains")
            result = cursor.execute("DELETE FROM contains WHERE 1=1")
            print("Clearing stock")
            result = cursor.execute("DELETE FROM stock WHERE 1=1")
            print("Clearing item")
            result = cursor.execute("DELETE FROM item WHERE 1=1")
            print("Clearing product_rating")
            result = cursor.execute("DELETE FROM product_rating WHERE 1=1")
            print("Clearing vendor_rating")
            result = cursor.execute("DELETE FROM vendor_rating WHERE 1=1")
            print("Clearing product")
            result = cursor.execute("DELETE FROM product WHERE 1=1")
            print("Clearing price")
            result = cursor.execute("DELETE FROM price WHERE 1=1")
            print("Clearing quantity")
            result = cursor.execute("DELETE FROM quantity WHERE 1=1")
            print("Clearing vendor")
            result = cursor.execute("DELETE FROM vendor WHERE 1=1")
            print("Clearing city")
            result = cursor.execute("DELETE FROM city WHERE 1=1")
    
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
    
    flag = response == 'y'
    flag = flag or response == 'Y'
    
    if not flag:
        db_name = input("Enter name of LastList database:\n")
        db_host = input("Enter host:\n")
        db_user = input("Enter username:\n")
        db_password = input("Enter password:\n")
    else:
        db_name = 'LastList'
        db_host = 'localhost'
        db_user = 'root'
        db_password = 'password123'

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
        print("Generating data. This will take a while")
        dicts = package_all_data()
        populate_vendor_and_city(dicts["city"], dicts["vendor"])
        populate_product(dicts["product"])
        populate_price(dicts["price"])
        populate_quantity(dicts["quantity"])
        populate_item(dicts["item"])
        populate_stock(dicts["stock"])
        print("####################")
        print("Population complete!")
        print("####################")
        
if __name__ == "__main__":
    main()
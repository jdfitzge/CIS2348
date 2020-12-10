#1374331 josh fitzgerald

from datetime import date
import sqlite3
import pandas as pd

conn = sqlite3.connect('final_project.db')   #database connection
c = conn.cursor()

todays_date = date.today()
#cond = 'damaged'

def main():      #main program
    print_menu()

def get_input():  #input menu
    print()
    print('ELECTRONICS INVENTORY PROGRAM (EIP)')
    print()
    print('Select the letter of the report you would like to run')
    print()
    print('a - Full Inventory Report                 p - Past Service Date Inventory Report')
    print('b - Laptop Inventory Report               x - Damaged Inventory Report')
    print('c - Tower Inventory Report                i - Item Lookup')
    print('d - Phone Inventory Report')
    print('o - Other Items Inventory Report')
    print()
    print('Select "q" to end program')
    return input()

def print_menu():             #menu queries and actions
    while(True):
        user_input = get_input()

        if(user_input=='a'):
            print('Full Inventory Report')
            print()
            c.execute('''SELECT * FROM FullInventory''')
            for r in c.fetchall():
                print(r)
            csv_write = pd.read_sql('SELECT * from FullInventory', conn) #csv report output
            csv_write.to_csv('FullInventory.csv', index=False)

        if(user_input=='b'):
            print('Laptop Inventory Report')
            print()
            c.execute('''SELECT * FROM FullInventory WHERE item_type = 'laptop' ORDER BY item_id''')
            for r in c.fetchall():
                print(r)
            csv_write = pd.read_sql('''SELECT * FROM FullInventory WHERE item_type = 'laptop' ORDER BY item_id''', conn)
            csv_write.to_csv('LaptopInventory.csv', index=False)

        if(user_input=='c'):
            print('Tower Inventory Report')
            print()
            c.execute('''SELECT * FROM FullInventory WHERE item_type = 'tower' ORDER BY item_id''')
            for r in c.fetchall():
                print(r)
            csv_write = pd.read_sql('''SELECT * FROM FullInventory WHERE item_type = 'tower' ORDER BY item_id''', conn)
            csv_write.to_csv('TowerInventory.csv', index=False)

        if(user_input=='d'):
            print('Phone Inventory Report')
            print()
            c.execute('''SELECT * FROM FullInventory WHERE item_type = 'phone' ORDER BY item_id''')
            for r in c.fetchall():
                print(r)
            csv_write = pd.read_sql('''SELECT * FROM FullInventory WHERE item_type = 'phone' ORDER BY item_id''', conn)
            csv_write.to_csv('TowerInventory.csv', index=False)

        if(user_input=='o'):
            print('Other Inventory Report')
            print()
            c.execute('''SELECT * FROM FullInventory WHERE item_type != 'phone' AND item_type != 'tower' 
            AND item_type != 'laptop' ORDER BY item_id''')
            for r in c.fetchall():
                print(r)
            csv_write = pd.read_sql('''SELECT * FROM FullInventory WHERE item_type != 'phone' AND item_type != 'tower' 
            AND item_type != 'laptop' ORDER BY item_id''', conn)
            csv_write.to_csv('OtherInventory.csv', index=False)

        if (user_input == 'p'):
            print('Past Service Date Inventory Report')
            print()
            c.execute('''SELECT * FROM PastServiceDateInventory WHERE service_date < "todays_date" ''')
            for r in c.fetchall():
                print(r)
            csv_write = pd.read_sql('''SELECT * FROM PastServiceDateInventory WHERE service_date < "todays_date"''', conn)
            csv_write.to_csv('PastServiceDateInventory.csv', index=False)

        if (user_input == 'x'):
            print('Damaged Inventory Report')
            print()
            c.execute('''SELECT * FROM DamagedInventory WHERE service_date < "todays_date" ''')
            for r in c.fetchall():
                print(r)
            csv_write = pd.read_sql('''SELECT * FROM DamagedInventory WHERE service_date < "todays_date"''', conn)
            csv_write.to_csv('DamagedInventory.csv', index=False)

        if (user_input == 'i'):  #inventory item lookup
            print('Item Lookup')
            print()
            mf = input('Enter the manufacturer name:')
            mf_lookup = 'SELECT EXISTS (SELECT *  FROM FullInventory WHERE manufacturer LIKE "%' + mf + '%");'
            mf_results = c.execute(mf_lookup)

            if mf_results.fetchone()[0] == 1:
                print()
                it = input('Enter a type of electronic:')
                it_lookup = 'SELECT EXISTS (SELECT FullInventory.* FROM FullInventory LEFT JOIN PastServiceDateInventory on FullInventory.item_id = PastServiceDateInventory.item_id WHERE FullInventory.cond ' \
                                            'IS NULL AND FullInventory.manufacturer LIKE "%' + mf + '%" AND FullInventory.item_type LIKE "%' + it + '%" AND PastServiceDateInventory.item_id IS NULL ORDER BY price)'
                it_results = c.execute(it_lookup)
                if it_results.fetchone()[0] == 1:
                        f_results = 'SELECT FullInventory.* FROM FullInventory LEFT JOIN PastServiceDateInventory on FullInventory.item_id = PastServiceDateInventory.item_id WHERE FullInventory.cond ' \
                                    'IS NULL AND FullInventory.manufacturer LIKE "%' + mf + '%" AND FullInventory.item_type LIKE "%' + it + '%" AND PastServiceDateInventory.item_id IS NULL ORDER BY price'
                        p_results = c.execute(f_results)
                        print()
                        print("Your item is:")
                        print()
                        print(p_results.fetchone())
                        print()
                        print("You may also consider")
                        for r in p_results.fetchall():
                            print(r)
                else:
                    print()
                    print("No such item in inventory")
                    print()

            else:
                print()
                print("No such item in inventory")
                print()

        if(user_input=='q'):
            break

if __name__ == "__main__":
    main()

#jdfitzge 1374331

from pathlib import Path
Path('final_project.db').touch()

import sqlite3
conn = sqlite3.connect('final_project.db')
c = conn.cursor()

import pandas as pd

DamagedInventory = pd.read_csv(r'C:\Users\joshua.fitzgerald\Desktop\FinalProject\DamagedInventory.csv')
DamagedInventory.to_sql('DamagedInventory', conn, if_exists='append', index = False)

FullInventory = pd.read_csv(r'C:\Users\joshua.fitzgerald\Desktop\FinalProject\FullInventory.csv')
FullInventory.to_sql('FullInventory', conn, if_exists='append', index = False)

LaptopInventory = pd.read_csv(r'C:\Users\joshua.fitzgerald\Desktop\FinalProject\LaptopInventory.csv')
LaptopInventory.to_sql('LaptopInventory', conn, if_exists='append', index = False)

ManufacturerList = pd.read_csv(r'C:\Users\joshua.fitzgerald\Desktop\FinalProject\ManufacturerList.csv')
ManufacturerList.to_sql('ManufacturerList', conn, if_exists='append', index = False)

PastServiceDateInventory = pd.read_csv(r'C:\Users\joshua.fitzgerald\Desktop\FinalProject\PastServiceDateInventory.csv')
PastServiceDateInventory.to_sql('PastServiceDateInventory', conn, if_exists='append', index = False)

PriceList = pd.read_csv(r'C:\Users\joshua.fitzgerald\Desktop\FinalProject\PriceList.csv')
PriceList.to_sql('PriceList', conn, if_exists='append', index = False)


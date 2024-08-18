import pandas as pd
import csv
from datetime import datetime
from data_entry import *
class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMS = ["date","amount","category","description"]
    @classmethod
    def initalize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns= cls.COLUMS)
            df.to_csv(cls.CSV_FILE, index=False)
    
    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry = {
            "date" : date,
            "amount" : amount,
            "category" : category,
            "description" : description
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMS)
            writer.writerow(new_entry)
        print("Entry added successfully")

def add():
    CSV.initalize_csv()
    date = get_date("Enter the date (dd-mm-yyyy) or hit enter for today: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date,amount,category,description)

add()
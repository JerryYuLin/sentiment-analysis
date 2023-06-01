import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb://localhost:27017/")


df = pd.read_csv("new_data.csv")
data = df.to_dict(orient="records")

db = client["sentiment-analysis"]
db.dataset.insert_many(data)


# insert_many(), insert_one()

# find(), find_one()

# update_one(), update_many(), replace_one()

# delete_one(), delete_many()

from pymongo import MongoClient

#create mongo client connection
client = MongoClient("mongodb://localhost:27017/")

#create new database for todoApp
mydb = client["todoDB"]

#create new collection from database in todoApp
mycol = mydb["taskList"]


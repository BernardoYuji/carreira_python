from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["escola"]
estudantes = db["estudantes"]

estudantes.insert_one({"nome": "Bernardo", "idade": 19})

for estudantes in estudantes.find():
    print(estudantes)
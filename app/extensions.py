from flask_pymongo import PyMongo
from flask import Flask
from pymongo import MongoClient

#Add mongo uri i've deleted mine as it contains my database access password or simply use
#mongodb:https//localhost:<port>/database
mongo=MongoClient("")
db=mongo.get_database("repo_db")
users= db.get_collection("users")
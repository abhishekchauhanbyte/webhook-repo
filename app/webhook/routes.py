from flask import Blueprint, json, request,render_template,redirect
from app import templates
from flask_pymongo import PyMongo
from app.extensions import mongo,db,users
import datetime


webhook = Blueprint('Webhook', __name__, url_prefix='/webhook',template_folder="templates")


@webhook.route('/receiver', methods=["POST"])
def receiver():
    if request.method=="POST":
        req_data=request.get_json()
        prevIndex=users.count_documents({})

        #adding objects into database
        users.insert_one({"action":req_data['action'],
                          "author":req_data["assignee"]['login'],
                          "from_branch":req_data["pull_request"]["base"]["ref"],
                          "to_branch": req_data["pull_request"]["head"]["ref"],
                          "dateTime":datetime.datetime.now(),
                          "index":prevIndex+1,
                          })
    if request.headers['Content-Type']=='application/json':
        my_info= json.dumps(request.json)
        print(my_info)
        return my_info
    return "Added"

@webhook.route('/')
def file():
    index=users.count_documents({})
    latest_data = users.find_one( {'index':index})
    return render_template("index.html" , data=latest_data)

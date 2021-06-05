from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from flask import Blueprint, jsonify, request, Flask
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient

import bcrypt
import datetime
import validators
from bson import json_util
from bson.json_util import dumps
import json
from dotenv import load_dotenv
import os
import smtplib
from itsdangerous import URLSafeTimedSerializer, URLSafeSerializer
load_dotenv()
import ssl

# mongo db connection
Connection = os.getenv("MONGO_SRI")
client = MongoClient(Connection, ssl_cert_reqs=ssl.CERT_NONE)
db = client["autos_db"]
collection = db["affil"]
emailAddress = os.getenv("BASE_EMAIL")
emailPassword = os.getenv("BASE_P")


# register blueprint
signUpEndPoint = Blueprint("signUpEndPoint", __name__)


@signUpEndPoint.route("/signup", methods=["POST"])
def createacc():

    data = request.json
    email = data["email"]
    password = data["password"]
    username = data["username"]

    if not email:
        return "email is missing", 400
    if not password:
        return "password is missing", 400
    if not username:
        return "username is missing", 400

    if validators.email(email) != True:
        return "Boba says email is not valid", 400

    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(12))

    checkEmail = collection.find_one({"email": email})
    checkUsername = collection.find_one({"username": username})

    if checkUsername != None:
        return "username is already taken..", 400

    if checkEmail is None:

        collection.insert({
            "email": email,
            "username": username,
            "password": hashed,
            "date": datetime.datetime.utcnow(),
        })

        access_token = create_access_token(identity={"email": email})

        mail(username, email)

        res = jsonify({
            "message": "Account has been created...",
            "token": access_token
        })

        return res, 200

    else:
        res = "you have an account already.."
        return res, 409


def mail(name, to):
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(emailAddress, emailPassword)

        subject = "MrKay Autos; Welcome"
        body = f"Hi {name}, Welcome to on board as an. we dont have money yet thats why we are using plain email. soon we would have Kala kala."

        msg = f'subject:  {subject}\n\n{body}'

        #smtp.sendmail(emailAddress, "gogechi8@gmail.com", msg)
        smtp.sendmail(emailAddress, to, msg)

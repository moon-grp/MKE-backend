from flask import Blueprint, jsonify, request, Flask
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from bson.json_util import dumps
from bson import json_util
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
import requests
import json


# mongo db connection
Connection = os.getenv("MONGO_SRI")
paystack = os.getenv("pAPI_KEY")
client = MongoClient(Connection)
db = client["frames_db"]
collection = db["orders"]

emailAddress = os.getenv("BASE_EMAIL")
emailPassword = os.getenv("BASE_P")


payEndPointU = Blueprint("payEndPointU", __name__)


@payEndPointU.route("/payproduct", methods=["POST"])
def view():

    data = request.json
    referenceCode = data["referenceCode"]
    customerName = data["customerName"]
    customerEmail = data["customerEmail"]
    customerPhone = data["customerPhone"]
    customerAddress = data["customerAddress"]
    productName = data["productName"]
    qtr = data["qtr"]

    verifyPayments = requests.get(f"https://api.paystack.co/transaction/verify/{referenceCode}",  headers={
        'Authorization': f'Bearer {paystack}'})

    data = json.loads(verifyPayments.content)

    transDate = data["data"]["transaction_date"]

    collection.insert_one({
        "CustomerName": customerName,
        "CustomerEmail": customerEmail,
        "CustomerPhone": customerPhone,
        "CustomerAddress": customerAddress,
        "Date": transDate,
        "ProductName": productName,
        "Quantity": qtr,
        "Data": data,
        "delivered": False

    })

    mail()

    return "Transaction successful..", 200


def mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(emailAddress, emailPassword)

        subject = "New Order"
        body = f"New Order just came in check dashboard."

        msg = f'subject:  {subject}\n\n{body}'

        #smtp.sendmail(emailAddress, "gogechi8@gmail.com", msg)
        smtp.sendmail(emailAddress, "mrkayenterprise@gmail.com", msg)

import pymongo
myurl="mongodb://localhost:27017"

dbConn=pymongo.MongoClient(myurl)
Dname=dbConn["SCMXpertLite"]    
Users=Dname["UserData"]
Shipment=Dname["ShipmentData"]
Feedback=Dname["Feedback"]



#JWT Token variables
class JWT_Token:
    SECRET_KEY = "secret"
    ALGORITHM = "HS256"
    EXPIRE_MINUTES=30

# Forgot Password Sender information
Sender_Mail="reddysekharamudala@gmail.com"
Sender_Mail_Password="qvraxbyckjekfdhj"

import json
import logging
from pymongo import MongoClient
import pymongo

from flask import Flask, request, jsonify, render_template

a = "mongodb+srv://yusufd:3yhM41JBmb85Klpu@cluster0.quv78ie.mongodb.net/test"

app = Flask(__name__)
client = MongoClient(a)

db = client["mydb"]
user = db['yus']


credentials = {
    "user": "",
    "password": ""



}

# @app.route('/users/<username>', methods=["GET"])
# def get_endpoint(username):
#     passwd = request.headers.get("Authorization")   THIS FOR AUTHORIZATION
#     if username == credentials['user'] and passwd == credentials['password']:
#         return credentials,200


@app.route('/users/', methods=["GET"])
def get_endpoint():
    result = list(user.find({}, {"_id": 0}))
    kullanicilar = []
    sifreler = []

    for i in range(len(result)):
        kullanicilar.append(result[i]["user"])
    for m in range(len(result)):
        sifreler.append(result[m]["password"])

    # return render_template('deneme.html', title='Welcome', kullanicilar=kullanicilar, sifreler = sifreler)
    return jsonify(msg="success", result=result), 200


@app.route('/', methods=["GET"])
def get_endpoint2():
    result = list(user.find({}, {"_id": 0}))
    kullanicilar = []

    for i in range(len(result)):
        kullanicilar.append(result[i]["user"])

    return render_template('deneme.html', title='Welcome', kullanicilar=kullanicilar)

# @app.route('/users/<y>', methods=["POST"])
# def post_endpoint(y):
#     credentials['user2'] = request.get_json()['yeniuser']
#     # db.firstcollection.insert_one(credentials)
#     credentials_backup = credentials

#     result = list(user.find({"user1":"yusuf"},{"_id":0}))
#     print(credentials)
#     return jsonify(msg="success", result= result) ,200


# @app.route('/users/<enteredname>', methods=['DELETE'])
# def delete_user(enteredname):
#     deleted = user.delete_many({"user": enteredname})
#     deletedcount = deleted.deleted_count
#     if deletedcount == 0:
#         return jsonify('öyle biri yok'), 200
#     return render_template('deneme.html', title='Welcome', enteredname=enteredname)
#     return jsonify({'silinen isim:': enteredname}), 200


# @app.route('/users/<y>', methods=["POST"])
# def post_endpoint(y):
#     data = request.get_json()
#     # credentials = {
#     #     "user":data['yeniuser'],
#     #     "password":data['yenipassword'],
#     # }
#     # credentials['user'] = request.get_json()['yeniuser']
#     # credentials['password'] = request.get_json()['yenipassword']
#     # credentials_backup = credentials
#     # print(credentials_backup)
#     user.insert_one({"user": data['yeniuser'],
#                     "password": data['yenipassword']})
#     result = list(user.find({}, {"_id": 0}))
#     # print(credentials)
#     return jsonify(msg="success", result=result),


@app.route('/add-user', methods=['POST'])
def add_user():
    data = request.json

    print(data)
    yeniuser = data['user']
    yenipassword = data['password']
    user.insert_one({'user': yeniuser, 'password': yenipassword})
    # return render_template('deneme2.html', title='Welcome')
    return 'OK', 200


@app.route('/delete-user', methods=['DELETE'])
def delete_user():
    data = request.json
    print(data)
    user.delete_one({"user": data['user'], "password": data['password']})
    return render_template('deneme.html', title='Welcome')


@app.route('/users/<update_name>', methods=["PUT"])
def update_user(update_name):
    yeniusername = request.get_json()
    result = user.update_many({"user": update_name}, {
                              "$set": {"user": yeniusername["yeni_isim"]}})
    if result.modified_count > 0:
        return jsonify(msg='user {} updated with {} succesfully'.format(update_name, yeniusername["yeni_isim"]))
    else:
        return jsonify(msg=f' {update_name} is not found'), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

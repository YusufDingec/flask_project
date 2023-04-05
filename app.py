import json
import logging
from pymongo import MongoClient
import pymongo

from flask import Flask, request, jsonify, render_template

a = "mongodb+srv://"

app = Flask(__name__)
client = MongoClient(a)

db = client["mydb"]
user = db['yus']


credentials = {
    "user": "",
    "password": ""



}


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

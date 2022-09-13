from flask import Flask,jsonify, render_template, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/users"
mongo = PyMongo(app)
user_collection = mongo.db.user

@app.route("/")
def form():
    return render_template("mongo.html")

@app.route("/read", methods = ['GET'])
def read():
    if request.method == 'GET':
        output = []
        for i in user_collection.find():
           print(i)
           output.append({ '_id': str(ObjectId(i['_id'])) , 'Name': i['Name'], 'Phone Number': i['Phone Number'], 'Location': i['Location']})
        return jsonify({'users': output})

@app.route("/create", methods = ['GET'])
def create():
    if request.method == 'GET':
        name = request.args.get('x')
        phone = request.args.get('y')
        loc = request.args.get('z')
        if name != "" and phone != "" and loc != "":
            user = user_collection.insert_one(
                {'Name': name,'Phone Number': phone,'Location': loc})
            return jsonify({'Name': name,'Phone Number': phone,'Location': loc,'Status': "Successfully Inserted"})
        else:
            return jsonify({'Status': "Unsuccessfully Inserted --> Please fill all the details first"}) 
                            
@app.route("/update", methods = ['GET'])
def update():
    if request.method == 'GET':
        id = request.args.get('id')
        field = str((request.args.get('field')))
        value = str((request.args.get('value')))
        filter = {'_id': ObjectId(id)}
        newvalues = {'$set': {field:value}}
        user_collection.update_one(filter,newvalues)
        return jsonify({'Status':"Successfully Updated"})

@app.route("/delete", methods = ['GET','DELETE'])
def delete():
    if request.method == 'GET':
        id = request.args.get('id')
        if id != "":
           user = user_collection.delete_one({'_id': ObjectId(id)})
           return jsonify({"Successfully Deleted": id})
        else:
            return jsonify({"Unsuccessfully Deleted":"Please fill the id first"})
if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')
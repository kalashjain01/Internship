from flask import Flask ,render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:tiger@localhost/user'
db = SQLAlchemy(app)

class viewuser(db.Model):
    __tablename__ = "viewuser"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    phone_number = db.Column(db.String(255),nullable=False)
    location = db.Column(db.String(255),nullable=False)
    
    def __init__(self, name, phone_number , location):
        self.name = name
        self.phone_number = phone_number
        self.location = location
    
    def __repr__(self):
        return f'{self.id}'

def format_event(event):
    return{
        "id" : event.id,
        "Name" : event.name,
        "Phone Number" : event.phone_number,
        "Location" : event.location
    }

@app.route('/')
def index():
    return render_template('app.html')


@app.route("/read", methods = ['GET'])
def read():
    if request.method == 'GET':
        events = viewuser.query.order_by(viewuser.id.asc()).all()
        event_List = []
        for event in events:
            event_List.append(format_event(event))
        return jsonify({'users': event_List})

@app.route("/create", methods = ['GET'])
def create():
    if request.method == 'GET':
        name = request.args.get('x')
        phone_number = request.args.get('y')
        location = request.args.get('z')
        if name != "" and phone_number != "" and location != "":
            new_user = viewuser(name, phone_number,location)
            db.session.add(new_user)
            db.session.commit()
            db.session.refresh(new_user)
            return jsonify({'Name':name,'Phone Number':phone_number,'Location':location,'Status': "Successfully Inserted"})
        else:
            return jsonify({'Status':"Unsuccessfully Inserted"})    


@app.route("/update", methods = ['GET'])
def update():
        id = request.args.get('id')
        field = request.args.get('field')
        if field == "Name":
            name = request.args.get('value')
            event=viewuser.query.filter_by(id=id)
            event.update(dict(name=name))
        elif field == "Phone Number":
            phone_number = request.args.get('value')
            event=viewuser.query.filter_by(id=id)
            event.update(dict(phone_number=phone_number))
        else:
            location = request.args.get('value')
            event=viewuser.query.filter_by(id=id)
            event.update(dict(location=location))     
        db.session.commit()
        return jsonify({'Status':"Successfully Updated"})

@app.route("/delete", methods = ['GET','DELETE'])
def delete():
     if request.method == 'GET':
        id = request.args.get('id')
        event= viewuser.query.filter_by(id=id).one()
        db.session.delete(event)
        db.session.commit()
        return jsonify({"Successfully Deleted": id })

if __name__ == "__main__":
    app.run(debug=True)
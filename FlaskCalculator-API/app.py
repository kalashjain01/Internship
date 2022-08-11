from flask import Flask,jsonify,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("app.html")

@app.route('/calculate', methods=['GET'])
def multiply():
    if request.method == 'GET':
        value1=int(request.args.get('value1'))
        value2=int(request.args.get('value2'))
        return jsonify({'Payload addition':value1+value2},
                   {'Payload subtraction':value1-value2}, 
                   {'Payload multiplication':value1*value2},
                   {'Payload division':value1/value2})

if __name__ == "__main__":
    app.run(debug=True , host='0.0.0.0')
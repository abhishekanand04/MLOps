from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to MLOps, I hope you are excited!"

@app.route("/ping")
def pinging():
    return "Hello, this is a ping "

@app.route('/user/<username>',methods=["GET"])
def show_user_profile(username):
    # show the user profile for that user
    return f'Hi {username}. Welcome to MLOps'

@app.route("/add", methods=["POST"])
def add_numbers():
    data = request.get_json()  # get JSON body
    num1 = data["num1"]
    num2 = data["num2"]
    return {"sum":num1+num2}



if __name__ == "__main__":
    app.run( port=8080,debug=True)
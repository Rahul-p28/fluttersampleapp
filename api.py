from flask import Flask, jsonify, request

app = Flask(__name__)


users = []

@app.route('/signup',methods=['POST'])
def register_user():
   
    data = request.get_json()
    print(data['email'])
    
    users.append(data['email'])
    return jsonify({"message": "User successfully registered!"}),200

@app.route('/login',methods=['POST'])
def get_registered_users():
    global registered_users
    data = request.get_json()
    for  i in users :
       if data['email'] == i :
           return jsonify({"message":"User Found"}),200
   
    return  jsonify({"message":"User Not Found"}),205      
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')


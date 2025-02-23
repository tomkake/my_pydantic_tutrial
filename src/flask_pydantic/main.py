from flask import Flask, request, jsonify
from pydantic import ValidationError
from models.user import User

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/", methods = ["POST"])
def post_user():
    if request.method == "POST":
        try:
            user_data = request.json
            user = User(**user_data)
            return jsonify(user.model_dump()), 200
        except ValidationError as e:
            # エラーメッセージを整形して出力
            return jsonify({"errors": e.errors()[0]["msg"]}), 400
        
        
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
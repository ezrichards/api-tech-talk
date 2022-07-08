from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/techtalk", methods=['GET'])
def techtalk():
    return "<h3>Nice work! See if you can send a POST request with a JSON body including the string \"message\" to <a href=\"https://localhost:8000/ilikecs\">https://localhost:8000/ilikecs</a></h3>"

@app.route("/ilikecs", methods=['POST'])
def ilikecs():
    print(request.get_json()['message'])
    return jsonify("Well done! Your message has been received.")

if __name__ == "__main__":
    app.run("0.0.0.0")
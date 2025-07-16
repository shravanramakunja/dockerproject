from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hey this is the Project I have pipelined to the docker container"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_word():
    try:
        return "Hello Thomas ! Aren't you surprised ? :D ", 200
    except Exception as e:
        return  str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

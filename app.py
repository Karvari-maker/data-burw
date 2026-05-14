from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Halo Bu RW, backend udah jalan di Railway!"

if __name__ == '__main__':
    app.run()

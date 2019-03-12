from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<html>Hi Hachimantai!</html>"


@app.route("/hachimantai")
def hachimantai():
    return "<html>スパルタキャンプ in 八幡平</html>"


@app.route("/goodbye")
def goodbye():
    return "<html>Good Bye!</html>"


"""
課題
http://127.0.0.1:5000/goodbye というURLを入力したら、「Good Bye!」と表示されるようにしてください
"""

if __name__ == '__main__':
    app.run(debug=True)

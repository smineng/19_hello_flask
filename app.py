import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<html>Hi Hachimantai!</html>"


@app.route("/hachimantai")
def hachimantai():
    return "<html>スパルタキャンプ in 八幡平</html>"


"""
課題
http://127.0.0.1:5000/goodbye というURLを入力したら、「Good Bye!」と表示されるようにしてください
"""

@app.route("/goodbye")
def goodbye():
    return "<html>Good Bye!</html>"


@app.route("/omikuji")
def omikuji():
    omikuji_list = ["大吉", "中吉", "吉", "凶", "大凶"]

    result = random.choice(omikuji_list)

    return f"あなたの今日の運勢は...{result}です！"


@app.route("/user/<username>")
def greet(username):
    return f"Hi {username}"





if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 假設這是我們的用戶數據庫
users = {
    "Alice": "123456",
    "Bob": "password",
    "Charlie": "test123",
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            return f"歡迎回來，{username}！"
        else:
            return "用戶名或密碼錯誤，請重試。"
    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if username in users:
            return "用戶名已存在，請更換。"
        elif password != confirm_password:
            return "密碼和確認密碼不一致，請重試。"
        else:
            users[username] = password
            return f"註冊成功，歡迎加入！"
    else:
        return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)

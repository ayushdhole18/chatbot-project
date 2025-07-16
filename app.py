from flask import Flask, render_template, request
from chatbot import get_response
import sqlite3

app = Flask(__name__)

# Log chat to SQLite
def log_chat(user, bot):
    conn = sqlite3.connect('conversation.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS chat (user_input TEXT, bot_reply TEXT)')
    c.execute('INSERT INTO chat (user_input, bot_reply) VALUES (?, ?)', (user, bot))
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        response = get_response(user_input)
        log_chat(user_input, response)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)

import psycopg2
from flask import Flask

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        dbname="mydb",
        user="user",
        password="password",
        host="db"
    )

@app.route("/")
def home():
    conn = connect_db()
    return "Connected to DB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

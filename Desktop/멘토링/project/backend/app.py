from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import MySQLdb
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASS = os.environ.get("DB_PASSWORD", "1234")
DB_NAME = os.environ.get("DB_NAME", "counter_db")

def get_db():
    return MySQLdb.connect(
        host=DB_HOST,
        user=DB_USER,
        passwd=DB_PASS,
        db=DB_NAME,
        charset="utf8"
    )

@app.route("/count/get", methods=["GET"])
def get_count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT value FROM counter WHERE id=1")
    value = cursor.fetchone()[0]
    db.close()
    return jsonify({"count": value})

@app.route("/count/increment", methods=["POST"])
def increment():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE counter SET value = value + 1 WHERE id=1")
    db.commit()
    cursor.execute("SELECT value FROM counter WHERE id=1")
    value = cursor.fetchone()[0]
    db.close()
    return jsonify({"count": value})

@app.route("/count/decrement", methods=["POST"])
def decrement():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE counter SET value = value - 1 WHERE id=1")
    db.commit()
    cursor.execute("SELECT value FROM counter WHERE id=1")
    value = cursor.fetchone()[0]
    db.close()
    return jsonify({"count": value})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

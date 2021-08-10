from flask import Flask

import os 
import psycopg2 

app = Flask(__name__)


@app.route('/')
def hello_world():
    with psycopg2.connect(f"dbname={os.getenv("DB_NAME")} user={"DB_USER"} password:{os.getenv:"DB_PASS"}") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM test;")
        rows = cur.fetchall() 
        message = ''
        for row in rows:
            message = message + row[1] 
    return message + " Direto de meu belo database!!"
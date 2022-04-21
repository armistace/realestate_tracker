from flask import Flask
from connector import connector

app = Flask(__name__)

@app.route("/houses")
def houses():
    conn = connector.connection()
    results = conn.get_houses()
    return_string = ""
    for result in results:
        return_string = return_string + result + " | "
    return return_string
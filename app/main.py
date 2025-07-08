import json
import os
from flask import Flask, render_template, request, redirect
import random
import string
from datetime import datetime

def write(origin, shorten):
    with open("db/db.json", "r") as file:
        data = json.load(file)

    if shorten in data.values():
        print("data sudah ada")
    else : 
        exp_date_raw = request.form.get("expire-date")
        exp_date = datetime.strptime(exp_date_raw, "%m/%d/%Y")
        data[shorten] = {
            "origin" : origin,
            "exp_date" : exp_date.isoformat()
        }
        with open("db/db.json", "w") as file:
            json.dump(data, file, indent=4)    
            print("UDAH REK")

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'template'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/shorten", methods=["POST"])
def shorten():
    unshorten = request.form.get("original-link", "")
    short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    write(unshorten, short)

    return render_template("index.html",
                           origin_link=unshorten,
                           short_link=short,
                           show_result=True)


@app.route("/<url_short>")
def routing(url_short):
    with open("db/db.json", "r") as f:
        data = json.load(f)

    entry = data.get(url_short)
    if not entry:
        return render_template("404.html"), 404


    now = datetime.now()
    exp_date = datetime.fromisoformat(entry["exp_date"])
    if now > exp_date:
        return render_template("exp.html"), 410  

    return redirect(entry["origin"], code=302)
 


if __name__ == "__main__":
    app.run(debug=True)

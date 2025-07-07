import json
import os
from flask import Flask, render_template

def write(origin, shorten):
    with open("db/db.json", "r") as file:
        data = json.load(file)

    if origin in data.values():
        print("data sudah ada")
    else :    
        data[shorten] = origin
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

if __name__ == "__main__":
    app.run(debug=True)

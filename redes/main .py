from flask import Flask, render_template, request

app = Flask(__name__)
lista = {}


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        lista[ request.form['Nome'] ] = request.form
        return render_template("listatelefonica.html", lista = lista.values())
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
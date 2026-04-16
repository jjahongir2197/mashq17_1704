from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def color():

    if request.method == "POST":

        color = request.form["color"]

        return f"Siz tanlagan rang: {color}"

    return render_template("index.html")

app.run(debug=True)

import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request, url_for

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():

    if not request.form.get("firstname") or not request.form.get("lastname") or not request.form.get("car"):
        return render_template("error.html", message="You need to fill form, min three fields")
    with open("survey.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["Firstname", "Lastname", "Car", "Color", "Person", "Dog", "Cat", "Others"])
        writer.writerow({"Firstname": request.form.get("firstname"), "Lastname": request.form.get("lastname"), "Car": request.form.get("car"),
                         "Color": request.form.get("color"), "Person": request.form.get("count"), "Dog": request.form.get("dog"), "Cat": request.form.get("cat"),
                         "Others": request.form.get("others")})
    #Перехід на сторінку таблиці
    return redirect(url_for("get_sheet"))


@app.route("/sheet", methods=["GET"])
def get_sheet():
    data = []
    # Відкриття CSV-файлу для читання
    with open('survey.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    return render_template('sheet.html', data=data)


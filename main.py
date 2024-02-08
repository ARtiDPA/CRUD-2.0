from flask import Flask, render_template, request
from sqlalchemy import insert, select
from database import connect
from models import user

app = Flask(__name__)


def add_insert(name, surname, age, gender):
    stmt = insert(user).values(name=name, suename=surname, age=age, gender=gender)
    connect.execute(stmt)
    connect.commit()


def read_select(index):
    query = select(user).filter(user.id == index)
    users = connect.execute(query)
    elemnts = [users.one()]
    return elemnts


def read_select_all():
    query = select(user)
    users = connect.execute(query)
    elements = users.all()
    return elements


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        age = request.form["age"]
        gender = request.form["gender"]
        if name != "" and surname != "" and age != "" and gender != "":
            add_insert(name, surname, age, gender)
            return "Успешно добавленно"
        else:
            return "Значения не могут быть пустыми"
    else:
        return render_template("add.html")


@app.route("/read", methods=["POST", "GET"])
def read():
    if request.method == "POST":
        index = request.form["index"]
        if int(index) == 0:
            elements = read_select_all()
            return render_template("read.html", elements=elements)
        else:
            elements = read_select(index)
            return render_template("read.html", elements=elements)
    else:
        return render_template("read.html")    


if __name__ == "__main__":
    app.run()

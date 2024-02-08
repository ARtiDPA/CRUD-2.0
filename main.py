from flask import Flask, render_template, request
from sqlalchemy import insert, select, delete
from database import connect
from models import user

app = Flask(__name__)


def delete_fun(index):
    stmt = delete(user).where(user.id == index)
    connect.execute(stmt)
    connect.commit()


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
def add_dec():
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
def read_dec():
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


@app.route("/delete", methods=["POST", "GET", "DELETE"])
def delete_dec():
    if request.method == "POST":
        id = request.form["index"]
        if id != 0:
            delete_fun(id)
            return f"Строка с id: {id}, удалилась"
        else:
            return "Нет строки с id 0"
    else:
        return render_template("delete.html")    


@app.route("/update", methods=["POST", "GET", "PUT"])
def update_dec():
    if request.method == "POST":
        id = request.form["index"]


if __name__ == "__main__":
    app.run()

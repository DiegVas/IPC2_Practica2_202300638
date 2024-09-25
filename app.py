# app.py
from flask import Flask, render_template, url_for, flash, redirect, request
from classes.car import Car

app = Flask(__name__)


userName = "empleado"
passWord = "$uper4utos#"

# settings
app.secret_key = "mysecretkey"

carsRegistered = []

userLogged = False


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    global userLogged
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        if user == userName and password == passWord:
            userLogged = True
            return redirect(url_for("Home"))
        else:
            flash("400")
            print("Un usuario ha intentado loguearse")
            return redirect(url_for("index"))

    return


@app.route("/Home")
def Home():
    global userLogged
    print(userLogged)
    if userLogged:
        return render_template("Home.html", Cars=carsRegistered)
    else:
        return redirect(url_for("index"))


@app.route("/delete/<string:Placa>", methods=["POST"])
def delete(Placa):
    for car in carsRegistered:
        if car.Placa == Placa:
            carsRegistered.remove(car)
    return redirect(url_for("Home"))


@app.route("/Add")
def Add():
    if userLogged:
        return render_template("Add.html")
    else:
        return redirect(url_for("index"))


@app.route("/added", methods=["POST"])
def added():
    if request.method == "POST":
        placa = request.form["Placa"]
        brand = request.form["brand"]
        model = request.form["model"]
        description = request.form["description"]
        unit_price = request.form["unit_price"]
        quantity = request.form["quantity"]
        image = request.form["image_url"]

        if any(car.Placa == placa for car in carsRegistered):
            flash("La placa ya está registrada")
            return redirect(url_for("Add"))

        new_car = Car(placa, brand, model, description, unit_price, quantity, image)
        carsRegistered.append(new_car)
        print("Se ha registrado un nuevo auto")
        return redirect(url_for("Home", Cars=carsRegistered))
    return


if __name__ == "__main__":
    app.run(port=3000, debug=True)

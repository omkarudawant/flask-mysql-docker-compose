from flask import Flask, request, jsonify
from config import config
import mysql.connector

app = Flask(__name__)


with app.app_context():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    with open("init_db.sql") as f:
        for line in f.readlines():
            print(line)
            try:
                cursor.execute(line)
            except mysql.connector.errors.ProgrammingError:
                pass
    print("Initialized DB")


@app.route("/user_management", methods=["GET", "POST"])
def user_manager():
    if request.method == "GET":
        username = request.get_json("username")
        with app.app_context():
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()
            response = cursor.execute(
                "SELECT name from user WHERE name LIKE ", username, ";"
            )
        return jsonify(response)

    elif request.method == "POST":
        username = request.get_json("username")
        email = request.get_json("email")
        password = request.get_json("password")
        mobile = request.get_json("mobile")
        profile_picture = request.files["profile_picture"]
        profile_picture = "tests"
        address = request.get_json("address")
        flat_number, addr1, addr2, city, state, pin = address.split(",")

        with app.app_context():
            connection = mysql.connector.connect(**config)
            cursor = connection.cursor()
            user_response = cursor.execute(
                "INSERT INTO user VALUES (",
                username,
                email,
                password,
                mobile,
                profile_picture,
                address,
                ");",
            )

            addr_response = cursor.execute(
                "INSERT INTO address VALUES (",
                flat_number,
                addr1,
                addr2,
                city,
                state,
                pin,
                ");",
            )
    return jsonify([user_response, addr_response])


if __name__ == "__main__":
    app.run()
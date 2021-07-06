# from flask import Flask, render_template
# app = Flask(__name__)

# my_list = [
#     {"name": "Link", "weapon": "master sword", "health": 3},
#     {"name": "Mario", "weapon": "Fireball", "health": 2},
#     {"name": "Pikachu", "weapon": "lightning", "health": 100},
# ]

# @app.route('/')
# def main_page():
#     return render_template("index.html", list=my_list)

# @app.route('/<name>/<weapon>/<int:health>')
# def add_character(name, weapon, health):
#     my_list.append({"name": name, "weapon": weapon, "health": health})
#     return render_template("index.html", list=my_list)

# if __name__ == "__main__":
#     app.run(debug=True)
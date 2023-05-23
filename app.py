# Import Flask and dependencies
from flask import Flask, render_template

# Create an app, being sure to pass __name__
app = Flask(__name__)

# Define what to do when a user goes to the index route
@app.route("/")
def Home():
    return render_template("Home.html")

# Items in this area are intended for V2
@app.route("/Conditions")
def Conditions():
    return render_template("Conditions.html")

@app.route("/Armor_and_Weapons")
def Armor_and_Weapons():
    return render_template("Armor_and_Weapons.html")

@app.route("/Actions")
def Actions():
    return render_template("Actions.html")

@app.route("/Other_Rules")
def Other_Rules():
    return render_template("Other_Rules.html")

@app.route("/Creating_Abilities")
def Creating_Abilities():
    return render_template("Creating_Abilities.html")

@app.route("/Core_Game_Rules")
def Core_Game_Rules():
    return render_template("Core_Game_Rules.html")

@app.route("/Character_Creation")
def Character_Creation():
    return render_template("Character_Creation.html")

# V2 Home page

@app.route("/V1_Home")
def V1_Home():
    return render_template("V1_Home.html")

if __name__ == "__main__":
    app.run(debug=True)
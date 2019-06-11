from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route('/')
def index():
    db = connectToMySQL("crpets")
    pets = db.query_db("SELECT * FROM pets;")
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/create_pet", methods=["POST"])
def add_pet_to_db():

    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(nm)s, %(ty)s, NOW(), NOW());"
    data = {
        "nm": request.form["names"],
        "ty": request.form["types"]
    }
    db = connectToMySQL ("crpets")
    db.query_db(query, data)
    return redirect("/")
    # QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
    #                         VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());
            
if __name__ == "__main__":
    app.run(debug=True)



"""Flask app for Cupcakes"""

from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from secrets import secret_key

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

# ROUTES FOR THE RESTFUL API, RETURNING JSON

@app.route('/api/cupcakes')
def retrieve_cupcakes(): 
    """Returns JSON for all cupcakes"""

    cupcakes = Cupcake.query.all()
    serialized_cupcakes = [c.serialize() for c in cupcakes]

    return jsonify(cupcakes=serialized_cupcakes)


@app.route("/api/cupcakes/<int:cupcake_id>")
def retrieve_single_cupcake(cupcake_id):
    """Return JSON for single cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized_cupcake = cupcake.serialize()

    return jsonify(cupcake=serialized_cupcake)

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create cupcake & return it in JSON"""

    flavour = request.json["flavour"]
    size = request.json["size"]
    rating = request.json['rating']
    image = request.json['image'] or None

    new_cupcake = Cupcake(flavour=flavour, size=size, rating=rating, image=image)

    db.session.add(new_cupcake)
    db.session.commit()

    response = jsonify(cupcake=new_cupcake.serialize())

    # Return with status code 201 --- return tuple (json, status)
    return (response, 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """Update a particular cupcake and respond with JSON of the updated instance"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    data = request.json

    cupcake.flavour = data.get('flavour', cupcake.flavour)
    cupcake.size = data.get('size', cupcake.size)
    cupcake.rating = data.get('rating', cupcake.rating)
    cupcake.image = data.get('image', cupcake.image)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """Deletes a particular cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="deleted")

# ROUTES FOR THE WEBSITE, RETURNING HTML

@app.route('/')
def homepage(): 
    """test"""

    cupcakes =  Cupcake.query.all() 

    return render_template('index.html', cupcakes=cupcakes)

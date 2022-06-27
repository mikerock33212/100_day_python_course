from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint, choice

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        # method 1 loop through each column
        # dictionary = {}
        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        # method 2 we can do dictionary comprehension
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/random', methods=['GET', 'POST'])
def random():
    all_cafe = Cafe.query.all()
    # random_index = randint(0, len(all_cafe))
    # random_cafe = Cafe.query.get(random_index+1)
    # more simple way
    random_cafe = choice(all_cafe)
    # there are other way to jsonify
    # return jsonify(cafe={'id': random_cafe.id,
    #                      'name': random_cafe.name,
    #                      'map_url': random_cafe.map_url,
    #                      'img_url': random_cafe.img_url,
    #                      'location': random_cafe.location,
    #                      'amenities': {'seats': random_cafe.seats,
    #                                    'has_toilet': random_cafe.has_toilet,
    #                                    'has_wifi': random_cafe.has_wifi,
    #                                    'has_sockets': random_cafe.has_sockets,
    #                                    'can_take_calls': random_cafe.can_take_calls,
    #                                    'coffee_price': random_cafe.coffee_price}
    #                      })
    return jsonify(cafe=random_cafe.to_dict())


@app.route('/all', methods=['GET', 'POST'])
def all_cafes():
    all_cafe = Cafe.query.all()
    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafe])


@app.route('/search', methods=['GET', 'POST'])
def search():
    error_message = {
            'Not Found': 'Sorry, we do not have a cafe at that location.'
    }
    query_location = request.args.get('loc')
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error=error_message)

# HTTP GET - Read Record


# HTTP POST - Create Record


@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record


@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    cafe_to_update = db.session.query(Cafe).get(cafe_id)
    if cafe_to_update:
        updated_coffee_price = request.args.get('new_price')
        cafe_to_update.coffee_price = updated_coffee_price
        db.session.commit()
        return jsonify(response={'Success': 'Successfully updated coffee price.'}), 200
    else:
        return jsonify(error={'Not Found': 'Sorry a cafe with given id was not found in the db.'}), 404


# HTTP DELETE - Delete Record


@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    secret_key = 'TopSecretAPIKey'
    key = request.args.get('api_key')
    if key == secret_key:
        cafe_to_delete = db.session.query(Cafe).get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={'Success': 'Successfully deleted closed cafe.'}), 200
        else:
            return jsonify(error={'Not Found': 'Sorry a cafe with given id was not found in the db.'}), 404
    else:
        return jsonify(error={'Forbidden': 'Sorry that was not allowed. Make sure you have correct api key.'}), 403



if __name__ == '__main__':
    app.run(debug=True)

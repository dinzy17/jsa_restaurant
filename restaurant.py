from settings import *
import json

# Initializing database
db = SQLAlchemy(app)


class Restaurant(db.Model):
    '''Model for Restaurant'''
    __tablename__ = 'restaurant'  # table name
    id = db.Column(db.Integer, primary_key=True)  # primary key
    name = db.Column(db.String(50), nullable=False)
    cuisine = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    specialties = db.Column(db.String(200), nullable=False)

    # function to convert output to json
    def json(self):
        return {'id': self.id, 'name': self.name,
                'cuisine': self.cuisine, 'type': self.type,
                'price': self.price,
                'specialties': json.loads(self.specialties)}

    # function to create new restaurant
    def add_restaurant(request_data):
        new_restaurant = Restaurant(name=request_data['name'],
                                    cuisine=request_data['cuisine'],
                                    type=request_data['type'],
                                    price=request_data['price'],
                                    specialties=json.dumps(
                                    request_data['specialties']))
        db.session.add(new_restaurant)
        db.session.commit()

    # function to get all restaurants
    def get_all_restaurants():
        return [Restaurant.json(restaurant)
                for restaurant in Restaurant.query.all()]

    # function to get restaurants using id
    def get_restaurant(_id):
        restaurant = Restaurant.query.filter_by(id=_id).first()
        if restaurant is None:
            return {"error": "Restaurant not found!"}
        else:
            return [Restaurant.json(restaurant)]

    # function to update restaurant
    def update_restaurant(_id, request_data):
        restaurant = Restaurant.query.filter_by(id=_id).first()
        if restaurant is None:
            return {"error": "Restaurant not found!"}
        else:
            restaurant.name = request_data['name']
            restaurant.cuisine = request_data['cuisine']
            restaurant.type = request_data['type']
            restaurant.price = request_data['price']
            restaurant.specialties = json.dumps(request_data['specialties'])
            db.session.commit()
            return {"message": "Restaurant updated!"}

    # function to delete restaurant using id
    def delete_restaurant(_id):
        restaurant = Restaurant.query.filter_by(id=_id).first()
        if restaurant is not None:
            Restaurant.query.filter_by(id=_id).delete()
            db.session.commit()
            return {"message": "Restaurant deleted!"}
        else:
            return {"error": "Restaurant not found!"}

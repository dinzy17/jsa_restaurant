from restaurant import *
from flask import jsonify


@app.route('/restaurant/all', methods=['GET'])
def get_restaurants():
    '''route to GET all restaurants'''
    return jsonify({'Restaurants': Restaurant.get_all_restaurants()})


@app.route('/restaurant/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    '''route to GET restaurant by id'''
    return_value = Restaurant.get_restaurant(id)
    status = 500 if "error" in return_value else 200
    response = jsonify(return_value)
    response.status_code = status
    return response


@app.route('/restaurant/create', methods=['POST'])
def add_restaurant():
    '''route to CREATE new restaurant'''
    request_data = request.get_json()  # getting data from client
    Restaurant.add_restaurant(request_data)
    response = jsonify({"message": "Restaurant added"})
    response.status_code = 201
    return response


@app.route('/restaurant/<int:id>', methods=['PUT'])
def update_restaurant(id):
    '''route to UPDATE restaurant with PUT method'''
    request_data = request.get_json()
    return_value = Restaurant.update_restaurant(id, request_data)
    status = 500 if "error" in return_value else 200
    response = jsonify({"message": "Restaurant added"})
    response.status_code = status
    return response


@app.route('/restaurant/<int:id>', methods=['DELETE'])
def remove_restaurant(id):
    '''route to DELETE restaurant using the DELETE method'''
    return_value = Restaurant.delete_restaurant(id)
    status = 500 if "error" in return_value else 200
    response = jsonify(return_value)
    response.status_code = status
    return response


if __name__ == "__main__":
    app.run(debug=True)

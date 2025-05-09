from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for car listings
cars = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2020, "price_per_day": 50},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2019, "price_per_day": 45},
    {"id": 3, "make": "Ford", "model": "Mustang", "year": 2021, "price_per_day": 80}
]

# Endpoint to get list of cars
@app.route('/api/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

# Endpoint to book a car
@app.route('/api/book', methods=['POST'])
def book_car():
    data = request.json
    car_id = data.get('car_id')
    user_name = data.get('user_name')
    # In a real app, booking logic and database storage would be here
    if not car_id or not user_name:
        return jsonify({"error": "Missing car_id or user_name"}), 400
    # Check if car exists
    car = next((car for car in cars if car['id'] == car_id), None)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    return jsonify({"message": f"Car {car['make']} {car['model']} booked successfully by {user_name}."})

if __name__ == '__main__':
    app.run(debug=True)

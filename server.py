import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

# SQLite database file path
DATABASE = 'database.db'

def query_database(query, params=()):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route('/get_locations', methods=['GET'])
def get_locations():
    locations = query_database("SELECT * FROM locations")

    # Convert the list of tuples to a list of dictionaries
    locations = [dict(zip(['id', 'name', 'total_cars', 'timestamp'], location)) for location in locations]
    

    return jsonify(locations)


if __name__ == "__main__":
    app.run(debug=True)
# Functions to store location's data in a sqlite database

import sqlite3


def update_location(location_data):
    # Connect to the database
    conn = sqlite3.connect('database.db')

    # Create a cursor
    c = conn.cursor()

    # If the table doesn't exist, create it
    # 
    # Table structure:
    # id (text), name (text), total_cars (int), timestamp (int)
    c.execute("""CREATE TABLE IF NOT EXISTS locations (
        id text PRIMARY KEY NOT NULL UNIQUE,
        name text,
        total_cars int,
        timestamp int,
        longitude real,
        latitude real,
        link text
    )""")

    # Insert the data into the table if it doesn't exist, otherwise update it
    c.execute("""INSERT INTO locations VALUES (
        :id,
        :name,
        :total_cars,
        :timestamp,
        :longitude,
        :latitude,
        :link
    ) ON CONFLICT(id) DO UPDATE SET
        name = :name,
        total_cars = :total_cars,
        timestamp = :timestamp,
        longitude = :longitude,
        latitude = :latitude,
        link = :link
    """, location_data)

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()
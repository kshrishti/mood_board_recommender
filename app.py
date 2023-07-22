from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

# Function to fetch images from the database
def get_images_from_db(tags):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = "SELECT * FROM images WHERE tag1=? OR tag2=? OR tag3=?"
    cursor.execute(query, (tags, tags, tags))
    images = cursor.fetchall()
    conn.close()
    return images

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle AJAX request for fetching images
@app.route('/get_images', methods=['POST'])
def get_images():
    selected_tag = request.json['tag']
    images = get_images_from_db(selected_tag)
    return jsonify(images)

if __name__ == '__main__':
    app.run(debug=True)

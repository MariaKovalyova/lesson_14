from flask import Flask, jsonify

from db_work import *

app = Flask(__name__)

@app.route("/movie/<title>")
def get_title_page(title):
    return get_title(title)

@app.route('/movie/<int:y1>/to/<int:y2>')
def get_movies_by_years(y1:int, y2:int):
    return jsonify(get_year_to_year(y1, y2))

@app.route('/rating/<cat>')
def get_movies_by_rating(cat):
    return jsonify(get_by_rat(cat))

@app.route('/genre/<gen>')
def get_movies_by_genre(gen):
    return jsonify(get_genre(gen))

if __name__ == "__main__":
    """ 127.0.0.1:5000 - дефолтный IP-адрес """
    app.run(debug=True)

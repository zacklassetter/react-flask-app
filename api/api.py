from flask_cors import CORS
from flask import Flask
from flask import request
import sqlite3


def selectZip(zip):
    county = ''
    population = ''
    try:
        sqliteConnection = sqlite3.connect('data/zipcodes.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = f"""SELECT * from locations where zipcode == {zip}"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        row = records[0]
        county = row[1]
        population = row[2]
        

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            return county, population





app = Flask(__name__)
CORS(app)


@app.route('/create_phrase', methods=['POST'])
def get_create_phrase():
    request_data = request.get_json()
    name = request_data['name']
    name = to_pig_latin(name)
    zip_code = request_data['zip']
    county, population = selectZip(zip_code)
    if name == '':
        return ''
    elif county is None or county == '':
        return {'phrase': f'{name} zip code is invalid'}
    else:
        
        return {'phrase': f'{name} zip code is in {county} County and has a population of {population}'}

def to_pig_latin(name):
    name = name.lower()
    names = name.split(" ")
    res = ''
    for n in names:
        if n == '':
            continue
        i = 0
        for x, letter in enumerate(n):
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                i = x
                break
        res += ((n[i:len(n)]) + n[0:i] + ('ay' if i > 0 else 'way')).capitalize()
        res += ' '
    if res[0:len(res) - 1] != '':
        res = res[0:len(res) - 1] + '\'s'
    return res

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

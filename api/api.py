from flask_cors import CORS
from flask import Flask
from flask import request
import sqlite3

#finds the county and population of the given zipcode
def selectZip(zip):
    county = ''
    population = ''
    #tries to query my database
    try:
        sqliteConnection = sqlite3.connect('data/zipcodes.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        #Make query on database
        sqlite_select_query = f"""SELECT zip, county_name, population from locations where zip == \"{zip}\";"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        row = records[0]
        county = row[1]
        population = row[2]
        

        cursor.close()
    #logs an error if a conncection cannot be made to the database
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        #close the connection and return the data
        if sqliteConnection:
            sqliteConnection.close()
            return county, population

#finds the county, state, and total county population of the given zipcode
def getCountyPop(zip):
    county = ''
    population = ''
    state = ''
    try:
        sqliteConnection = sqlite3.connect('data/zipcodes.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        #Make query on database
        sqlite_select_query = f"""select county_name, state_name, sum(population) as pop from locations group by county_name,state_name having (county_name, state_name) in (select county_name, state_name from locations where zip == \"{zip}\");"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        row = records[0]
        county = row[0]
        state = row[1]
        population = row[2]
        

        cursor.close()

    #log error if connection cannot be made
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            return county, state, population



app = Flask(__name__)
CORS(app)

#handles a get request that takes a name and zipcode as parameters
@app.route('/create_phrase')
def get_create_phrase():
    name = request.args['name']
    zip_code = request.args['zip']
    name = to_pig_latin(name)
    county, population = selectZip(zip_code)
    if True in [char.isdigit() for char in name]:
        return {'phrase': 'Invalid name'}
    if name == '':
        return ''
    elif county is None or county == '':
        return {'phrase': f'{name} zip code is invalid'}
    else:
        
        return {'phrase': f'{name} zip code is in {county} County and has a population of {population}'}

#handles a get request that takes a zipcode as a parameter
@app.route('/county_pop')
def get_create_county():
    zip_code = request.args['zip']
    county, state, population = getCountyPop(zip_code)
    if zip_code == '':
        return ''
    elif county is None or county == '':
        return ''
    else:
        return {'phrase': f'{county} County is in {state} and has a population of {population}'}

#Transforms the given name into pig latin
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

#The front page to be displayed on the heroku app
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

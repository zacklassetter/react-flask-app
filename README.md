# This application is hosted on heroku 
- The front end is hosted at https://zero-react.herokuapp.com/
- The backend is hosted at https://zero-flask.herokuapp.com/

# To start the app locally
Navigate to the root directory of the project and type:

```
cd api
venv\Scripts\activate
cd ..
npm run start-api
```
This will start the backend of the project

To start the frontend, first open a new terminal window, navigate to the project and type
```
npm install 
```
This will install the project dependencies.
Next type:
```
npm start
```

The entire project now should be running locally

# Approach 
For the underlying data I found data in the form of a csv file from https://simplemaps.com/data/us-zips.
I then created a Sqlite database, created a corresponding schema, and then imported the csv file into my database.

To manage the first phrase, I created a single '\create_phrase' endpoint in the flask backend. It takes two parameters: a name and a zipcode. It then queries the database I created to find the corresponding county and population.

The additional feature that I implemented was another api endpoint '/county_pop', that takes a zipcode as a parameter. This then makes a more complicated query on my database which sums up the population of all of the zipcodes within the county of the given zipcode.

On the react side, I created four state variables, name, zip, phrase, and county_phrase. These store the entered name, entered zip code, phrase returned from my first endpoint, and data returned from my second endpoint respectively. I then used the useEffect hook to make get requests to my backend when the relevent state variables were updated.




import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [name, setName] = useState("");
  const [zip, setZip] = useState("");
  const [phrase, setPhrase] = useState("");
  const [countyPhrase, setCountyPhrase] = useState("");



  //name and zip code information to send to /create_phrase
  const json = JSON.stringify({
    name: name,
    zip: zip
  });

  //Every time the name or zipcode is updated, retrieve the new phrase and update the state
  useEffect(() => {
    axios.get('/create_phrase', { params: { name: name, zip: zip } })
    .then(res => setPhrase(res.data.phrase))
    .catch(error => {
      console.log(error);
    });
  }, [name, zip]);

  //zipcode to send to /county_pop
  const zipJson = JSON.stringify({
    zip: zip
  });


  //Every Time the zipcode is updated, retrieve information about the total population of the county
  //of the given zipcode
  useEffect(() => {
    axios.get('/county_pop', { params: { zip: zip } })
    .then(res => setCountyPhrase(res.data.phrase))
    .catch(error => {
      console.log(error);
    });
  }, [zip]);

  return (
    <div className="App">
      <div className="container">
        
          <div className="row py-4">
            
              <div className="display-5 py-1">Enter name and zipcode:</div>
                <form>
                  <div className="form-group py-1">
                    <label className="font-weight-bold" aria-label="name-input">Enter your name:</label>
                    <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
                  </div>
                  <div className="form-group py-1">
                    <label> Enter your zip code:</label>
                    <input type="text" value={zip} onChange={(e) => setZip(e.target.value)} />
                  </div>
                </form>
              </div>
            

            <div className="row">
          
            <div className="display-6 py-1">Information:</div>
            <p className="py-1" data-testid="phrase-component">{phrase}</p>
        
            <p className="py-1">{countyPhrase}</p>
          
          </div>
          
        
        
      </div>
    </div>
  );
}

export default App;

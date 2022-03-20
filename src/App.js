import logo from './logo.svg';
import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [name, setName] = useState("");
  const [zip, setZip] = useState("");
  const [phrase, setPhrase] = useState("");



  const json = JSON.stringify({
    name: name,
    zip: zip
  });
  useEffect(() => {
    axios.post('https://zero-flask.herokuapp.com//create_phrase', json, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(res => setPhrase(res.data.phrase))
    .catch(error => {
      // handle error
      console.log(error);
    });
  }, [name, zip]);

  return (
    <div className="App">
      <header className="App-header">

      <form>
      <label>Enter your name:
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
      </label>
      <label> Enter your zip code:
      <input type="text" value={zip} onChange={(e) => setZip(e.target.value)} />
      </label>
    </form>

        <p>{phrase}</p>
      </header>
    </div>
  );
}

export default App;

#!/usr/bin/node

const request = require('request');

request({
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  json: true
}, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  body.characters.forEach((character) => {
    request({ url: character, json: true }, (error, response, body) => {
      if (error) { console.log(error); }
      console.log(body.name);
    }
    );
  });
});

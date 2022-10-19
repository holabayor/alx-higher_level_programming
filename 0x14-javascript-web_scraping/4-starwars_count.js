#!/usr/bin/node

const request = require('request');
const character = 'https://swapi-api.hbtn.io/api/people/18/';
request({ url: process.argv[2], json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  let count = 0;
  body.results.forEach((task) => {
    if (task.characters.indexOf(character) > -1) {
      count++;
    }
  });
  console.log(count);
});

#!/usr/bin/node
// Script that returns the status code of a request

const request = require('request');

request(process.argv[2], (error, response) => {
  if (error) {
    console.log(error);
  }
  console.log('code:', response.statusCode);
});

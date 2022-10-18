#!/usr/bin/node
// Script that returns the status code of a request

const request = require('request');

const url = process.argv[2];
request(url, (error, response, body) => {
  console.log('code: ', response && response.statusCode);
});

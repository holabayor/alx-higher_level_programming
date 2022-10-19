#!/usr/bin/node

const request = require('request');

request({ url: process.argv[2], json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const result = {};
  body.forEach((task) => {
    if (task.completed === true) {
      if (result[task.userId]) {
        result[task.userId] += 1;
      } else result[task.userId] = 1;
    }
  });
  console.log(result);
});

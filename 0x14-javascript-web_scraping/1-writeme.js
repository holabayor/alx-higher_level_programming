#!/usr/bin/node
// Script that reads and prints the content of a file

const fs = require('fs');

const filepath = process.argv[2];
const content = process.argv[3];
fs.writeFile(filepath, content, 'utf-8', err => {
  if (err) {
    console.error(err);
  }
  // file written successfully
});

#!/usr/bin/node
// Script that prints a square
const len = process.argv[2];

if (typeof (args) !== Number) {
  console.log('Missing size');
}
for (let i = 0; i < len; i++) {
  for (let j = 0; j < len; j++) {
    console.log('X');
  }
}

#!/usr/bin/node
// defines a Square class
const SquareModel = require('./5-square');

module.exports = class Square extends SquareModel {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let character = c;
    if (!c) {
      character = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(character.repeat(this.size));
    }
  }
};

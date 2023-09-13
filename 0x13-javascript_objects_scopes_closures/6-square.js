#!/usr/bin/node
// Defining a class Square that inherits Rectangle
const SquareSuper = require('./5-square');

class Square extends SquareSuper {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let row = 0; row < this.height; row++) {
      let charToDisplay = '';
      for (let col = 0; col < this.width; col++) {
        charToDisplay += c;
      }
      console.log(charToDisplay);
    }
  }
}

module.exports = Square;

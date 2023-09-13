#!/usr/bin/node
// Defining a class Square that inherits Rectangle
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;

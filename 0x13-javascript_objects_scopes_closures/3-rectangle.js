#!/usr/bin/node
// Defining a class Rectangle

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let row = 0; row <= this.height; row++) {
      let charToDisplay = '';
      for (let col = 0; col <= this.width; col++) {
        charToDisplay += 'X';
      }
      console.log(charToDisplay);
    }
  }
}

module.exports = Rectangle;

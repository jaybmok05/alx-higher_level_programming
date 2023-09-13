#!/usr/bin/node
// Defining a class Rectangle

class Rectangle {
  // class rectangle cosntructor function
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  // methods
  print () {
    for (let row = 0; row < this.height; row++) {
      let charToDisplay = '';
      for (let col = 0; col < this.width; col++) {
        charToDisplay += 'X';
      }
      console.log(charToDisplay);
    }
  }

  rotate () {
    const holder = this.width;
    this.width = this.height;
    this.height = holder;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

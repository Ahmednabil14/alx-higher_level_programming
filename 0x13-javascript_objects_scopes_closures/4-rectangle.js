#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let j = 0; j < this.height; j++) {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const y = this.height;
    this.height = this.width;
    this.width = y;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;

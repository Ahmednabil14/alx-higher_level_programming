#!/usr/bin/node
const Parent = require('./5-square');
class Square extends Parent {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.height; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;

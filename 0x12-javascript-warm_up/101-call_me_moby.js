#!/usr/bin/node
function callMeMoby (x, theFunction) {
  for (let index = 0; index < x; index++) {
    theFunction();
  }
}
module.exports = { callMeMoby };

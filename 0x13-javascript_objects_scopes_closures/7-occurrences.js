#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  for (const obj of list) {
    if (obj === searchElement) {
      counter++;
    }
  }
  return (counter);
};

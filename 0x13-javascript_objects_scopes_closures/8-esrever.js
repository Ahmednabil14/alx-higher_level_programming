#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  let counter = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newList[counter] = list[i];
    counter++;
  }
  return (newList);
};

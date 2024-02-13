#!/usr/bin/node
exports.esrever = function (list) {
  let new_list = [];
  let counter = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    new_list[counter] = list[i];
    counter++;
  }
  return (new_list);
};

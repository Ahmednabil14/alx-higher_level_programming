#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map(function (element, index) {
  return (element * index);
});
console.log(list);
console.log(newList);

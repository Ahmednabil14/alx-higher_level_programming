#!/usr/bin/node
const dict = require('./101-data').dict;
const val = Object.values(dict);
const arrayDict = Object.entries(dict);
const newDict = {};
let valFilter = [];
valFilter = val.filter(function (ele) {
  if (!valFilter.includes(ele)) {
    valFilter.push(ele);
    return true;
  }
  return false;
});

for (const item of valFilter) {
  const arr = [];
  for (const ele of arrayDict) {
    if (ele[1] === item) {
      arr.push(ele[0]);
    }
  }
  newDict[item] = arr;
}
console.log(valFilter);
console.log(newDict);

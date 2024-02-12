#!/usr/bin/node

const x = process.argv;
let i = 0;
let j = 0;

if (x[3]) {
  for (let index = 2; index < x.length; index++) {
    if (Number(x[index]) > i) {
      i = x[index];
    }
  }
  for (let index = 2; index < x.length; index++) {
    if (Number(x[index]) < i && Number(x[index]) > j) {
      j = Number(x[index]);
    }
  }
  console.log(j);
} else {
  console.log(0);
}

#!/usr/bin/node

const x = process.argv[2];

if (parseInt(x)) {
  console.log(`My number: ${parseInt(x)}`);
} else {
  console.log('Not a number');
}

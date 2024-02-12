#!/usr/bin/node

const y = process.argv[2];

if (parseInt(y)) {
  let sq = '';
  for (let i = 0; i < y; i++) {
    sq += 'x';
  }
  for (let i = 0; i < y; i++) {
    console.log(sq);    
  }
} else {
    console.log('Missing size');
}

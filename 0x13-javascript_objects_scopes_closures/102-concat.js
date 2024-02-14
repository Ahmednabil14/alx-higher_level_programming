#!/usr/bin/node
const fs = require('fs');
let data = '';
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
fs.readFile(fileA, 'utf8', function (err, fileA) {
  if (err) {
    return;
  }
  if (fileA) {
    data += fileA + '\n';
  }
  fs.readFile(fileB, 'utf8', function (err, fileB) {
    if (err) {
      return;
    }
    if (fileB) {
      data += fileB + '\n';
    }
    fs.writeFile(fileC, data, function () {
    });
  }
  );
}
);

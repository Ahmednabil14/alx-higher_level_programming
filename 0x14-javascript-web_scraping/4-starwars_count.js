#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  const objs = JSON.parse(body).results;
  let count = 0;
  for (const obj of objs) {
    for (const char of obj.characters) {
      if (char.includes('18')) {
        count += 1;
      }
    }
  }
  return (count);
});

#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, resp) => {
  if (err) {
    console.log(err);
  }
  console.log(`code: ${resp.statusCode}`);
});

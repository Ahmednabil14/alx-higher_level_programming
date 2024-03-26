#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  /* body is string so you need to convert to json */
  console.log(JSON.parse(body).title);
});

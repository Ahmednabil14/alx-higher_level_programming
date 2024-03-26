#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  console.log(typeof(body))
  console.log(typeof(JSON.parse(body)))
  console.log(JSON.parse(body).title);
});

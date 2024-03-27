#!/usr/bin/node
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  const bodyObject = JSON.parse(body);
  const characters = bodyObject.characters;
  for (const char of characters) {
    request.get(char, (err, resp, body) => {
      if (err) {
        console.log(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});

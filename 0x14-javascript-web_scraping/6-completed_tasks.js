#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  }
  const users = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0
  };
  const objs = JSON.parse(body);
  for (const user in users) {
    console.log(typeof (user));
    for (const obj of objs) {
      if (obj.userId === user && obj.completed === true) {
        users[user] += 1;
      }
    }
  }
  console.log(users);
});

#!/usr/bin/node

const req = require('request');

const url = process.argv[2];

req.get(url, (err, urlResp) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${urlResp.statusCode}`);
  }
});

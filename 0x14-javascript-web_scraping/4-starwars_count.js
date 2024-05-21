#!/usr/bin/node

const req = require('request');
const url = process.argv[2];

req.get(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;
    console.log(films.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});

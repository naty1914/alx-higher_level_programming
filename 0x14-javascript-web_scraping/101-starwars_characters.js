#!/usr/bin/node

const req = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(body);
    const charactersUrls = movie.characters;

    charactersUrls.forEach((characterUrl, index) => {
      req.get(characterUrl, (err, resp, body) => {
        if (err) {
          console.log(err);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
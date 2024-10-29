#!/usr/bin/node
const req = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

req.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(body);
    const charactersUrls = movie.characters;
    displayCharacters(charactersUrls, 0);
  }
});
function displayCharacters (characterUrls, index) {
  if (index >= characterUrls.length) return;
  req.get(characterUrls[index], (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const character = JSON.parse(body);
      console.log(character.name);
      displayCharacters(characterUrls, index + 1);
    }
  });
}

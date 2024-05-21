#!/usr/bin/node
const file = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

file.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});

#!/usr/bin/node

const file = require('fs');
const filePath = process.argv[2];
file.readFile(filePath, 'utf8', (err, content) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(content);
});

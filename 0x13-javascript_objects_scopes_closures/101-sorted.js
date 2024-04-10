#!/usr/bin/node

const dict = require('./101-data').dict;
const newDictionary = {};
for (const value in dict) {
  const valueOccurence = dict[value];

  if (valueOccurence in newDictionary) {
    newDictionary[valueOccurence].push(value);
  } else {
    newDictionary[valueOccurence] = [value];
  }
}
console.log(newDictionary);

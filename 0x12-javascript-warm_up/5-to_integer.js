#!/usr/bin/node
const numArgument = process.argv[2];

if (numArgument !== undefined) {
  const number = parseInt(numArgument);

  if (!isNaN(number)) {
    console.log('My number:', number);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}

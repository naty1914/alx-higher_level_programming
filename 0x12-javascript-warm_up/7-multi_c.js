#!/usr/bin/node
const numArgument = process.argv[2];
const m = 'C is fun';

if (numArgument !== undefined) {
  const number = parseInt(numArgument);

  if (!isNaN(number)) {
    for (let i = 0; i < number; i++) {
      console.log(m);
    }
  }
} else {
  console.log('Missing number of occurrences');
}

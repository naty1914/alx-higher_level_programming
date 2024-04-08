#!/usr/bin/node
const numArgument = process.argv[2];
const m = 'X';

if (numArgument !== undefined) {
  const number = parseInt(numArgument);

  if (!isNaN(number)) {
    for (let i = 0; i < number; i++) {
      let r = '';
      for (let i = 0; i < number; i++) {
        r += m + '';
      }
      console.log(r);
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}

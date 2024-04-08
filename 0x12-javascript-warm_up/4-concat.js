#!/usr/bin/node
const numArguments = process.argv.length - 2;
if (numArguments === 0) {
  console.log(process.argv[2] + ' is ' + process.argv[2]);
} else if (numArguments === 1) {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}

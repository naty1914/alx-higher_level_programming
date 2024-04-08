#!/usr/bin/node
const numArguments = process.argv[2];
if (numArguments === undefined) {
  console.log('No argument');
} else {
  console.log(numArguments);
}

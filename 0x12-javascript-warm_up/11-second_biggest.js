#!/usr/bin/node
const argument = process.argv.slice(2);

const num = argument.map(arg => parseInt(arg));

const sortednum = num.sort((a, b) => b - a);
const secondBiggestNumber = sortednum[1] || 0;
console.log(secondBiggestNumber);

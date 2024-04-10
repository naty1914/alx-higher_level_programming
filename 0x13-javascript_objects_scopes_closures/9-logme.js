#!/usr/bin/node
let c = 0;
exports.logMe = function (item) {
  for (let i = 0; i < arguments.length; i++) {
    console.log(c + ': ' + arguments[i]);
    c++;
  }
};

#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let j;
  for (j = 0; j < x; j++) {
    theFunction();
  }
};

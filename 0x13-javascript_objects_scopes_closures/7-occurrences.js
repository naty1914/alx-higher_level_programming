#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let _count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      _count++;
    }
  }
  return _count;
};

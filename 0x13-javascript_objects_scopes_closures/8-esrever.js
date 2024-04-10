#!/usr/bin/node
exports.esrever = function (list) {
  let listStart = 0;
  let listEnd = list.length - 1;
  while (listStart < listEnd) {
    const i = list[listStart];
    list[listStart] = list[listEnd];
    list[listEnd] = i;

    listStart++;
    listEnd--;
  }
  return list;
};

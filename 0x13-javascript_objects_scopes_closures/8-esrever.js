#!/usr/bin/node
// returns a reversed string
exports.esrever = function (list) {
  const newList = [];
  for (let idx = list.length - 1; idx >= 0; idx--) {
    newList.push(list[idx]);
  }
  return newList;
};

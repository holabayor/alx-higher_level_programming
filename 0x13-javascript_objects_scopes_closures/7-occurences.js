#!/usr/bin/node
// defines a Square class
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  list.forEach(element => {
    if (element === searchElement) {
      occurences += 1;
    }
  });
  return occurences;
};

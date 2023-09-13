#!/usr/bin/node
let argHolder = 0;
exports.logMe = function (item) {
  console.log(`${argHolder}: ${item}`);
  argHolder++;
};

// --- Directions
// Given an integer, return an integer that is the reverse
// ordering of numbers.
// --- Examples
//   reverseInt(15) === 51
//   reverseInt(981) === 189
//   reverseInt(500) === 5
//   reverseInt(-15) === -51
//   reverseInt(-90) === -9

const reverse = require('../reversestring');

function reverseInt(n) {
  const sign = Math.sign(n);
  reversed = parseInt(n.toString().split('').reverse().join(''));
  // return Math.sign(n) === -1 ? -1 * reverse : reverse;
  return Math.sign(n) * reversed;
}

module.exports = reverseInt;

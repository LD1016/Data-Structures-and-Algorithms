// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

const reverse = (str) => {
  return str.split('').reduce((reversed, character) => {
    return character + reversed;
  }, '');
};

/*
// Step1: place the location of debugger
// Step2: must call the functin here
// Step3: run the debugger mode : node inspect index.js
// c : for continue excution for the next debugger (each step of looping) 
// repl : is repl mode to inspect variable inside
// control C to exit

const reverse = (str) => {
  let reversed = '';
  for (let character of str) {
    reversed = character + reversed;
    debugger;                           // step 1
  }
  return reversed;
};

reverse('abcd');                       // step 2

*/
module.exports = reverse;

// const reverse = (str) => {
//   // const arr = str.split('');
//   // arr.reverse();
//   // return arr.join('');
//   return str.split('').reverse().join('');
// };

// const reverse = (str) => {
//   let reversed = '';
//   for (let character of str) {
//     reversed = character + reversed;
//   }
//   return reversed;
// };

#!/usr/bin/node
const firstNumber = Number(process.argv[2]);
if (firstNumber) {
  console.log(`My number: ${firstNumber}`);
} else {
  console.log('Not a number');
}

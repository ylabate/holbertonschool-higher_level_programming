#!/usr/bin/node
const x = process.argv[2];
if (isNaN(x)) {
  console.log('Missing size');
}

let row = '';
for (let j = 0; j < x; j++) {
  row += 'X';
}

for (let i = 0; i < x; i++) {
  console.log(row);
}

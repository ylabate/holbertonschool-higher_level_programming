#!/usr/bin/node
const [a, b] = process.argv.slice(2, 4).map(Number);
console.log(a + b);

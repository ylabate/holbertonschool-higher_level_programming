#!/usr/bin/node
function factorial (f) {
  if (isNaN(f)) { return 1; }
  if (f <= 1) {
    return f;
  }
  return f * factorial(f - 1);
}

console.log(factorial(Number(process.argv[2])));

const LIMIT = 1000;
let d = 0;
let poop = [];

function pentagonal(n) {
  return (n * (3 * n - 1)) / 2;
}

function isPentagonal(n) {
  let j = 1;
  let k = 0;

  do {
    k = pentagonal(j);
    j++;
  } while (k < n);

  return (k === n);
}

for (let i = 0; i < LIMIT - 1; i++) {
  for (let j = 1; j < LIMIT - 1; j++) {
    let pi = pentagonal(i);
    let pj = pentagonal(j);

    let sum = pi + pj;
    let diff = Math.abs(pi - pj);

    if (sum !== diff && isPentagonal(sum) && isPentagonal(diff)) {
      d = diff;
      poop = [sum, diff];
    }
  }
}

console.log(d, poop);

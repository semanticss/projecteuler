let p = 0;
let length = 200;

function t(n) {
    return 2 * (n^2) - 1;
}

function isPrime(n) {
    if (n % 2 !== 0 && n % 3 !== 0) return true;
}

for (let i = 1; i < length; i++) {
    const num = t(i);
    console.log(num);
    if (isPrime(num)) p++;
}

console.log(p);
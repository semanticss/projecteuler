let sum = 1n;
let g = 100n;

while (g > 1n) {
    sum *= g;
    g--;
}

console.log(sum);

digits = sum.toString().split("");

console.log(digits);

let s = 0;

for (let i = 0; i < digits.length - 1; i++) {
    s += Number(digits[i]);
}

console.log(s);
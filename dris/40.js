let num = "";
const LIMIT = 1_000_000;

for (let i = 1; i <= LIMIT; i++) {
    num += i.toString();
}

// console.log(num);

let answer = 1;

for (let i = 1; i <= LIMIT; i *= 10) {
    const number = Number(num[i - 1]);
    answer *= number;
    console.log(i, answer, number);
}

console.log(answer);

// 210
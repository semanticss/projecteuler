let a = 1, b = 2, sum = 2;

// for (let i = 0; terms[1] < (4 * 1000 * 1000); i++) {
//     let j = terms[0] + terms[1];
//     if (j % 2 === 0) sum += j;

//     terms.shift();
//     terms.push(j);
// }

while (b < 4_000_000) {
    c = a + b;
    if (c % 2 === 0) sum += c;
    a = b;
    b = c;
}

console.log(sum);
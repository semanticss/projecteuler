let num = 1;

function getFactors(num) {
    if (num < 4 || num % 2 !== 0 && num % 3 !== 0) return num; // check if prime
    return "not prime";
}

console.log(getFactors(num));
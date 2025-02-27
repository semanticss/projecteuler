function isPalindrome(num) {
    if (num.toString() === num.toString().split("").reverse().join("")) return num;
}

let last = 0;
for (let i = 99; i < 999; i++) {
    for (let j = 99; j < 999; j++) {
        let test = i * j;
        let isP = isPalindrome(test);
        if (isP > last) last = isP;
    }
}

console.log(last);
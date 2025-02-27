let nums = 0;
const POWER = 5;

function getPower(num) {
    let sum = 0;
    let arr = num.toString().split("");

    for (let i = 0; i < arr.length; i++) {
        // console.log(arr[i]);
        sum += Math.pow(Number(arr[i]), POWER);
    }

    if (sum === num) nums += num;
}


for (let i = 2; i < 10000000; i++) {
    // console.log(i);
    getPower(i);
}

console.log(nums);

// 443839
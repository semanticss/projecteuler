let length = 0;
let num = 0;

for (let i = 0; i < (1000 * 1000); i++) {
  let s = i;
  let l = 0;

  while (s > 1) {
    if (s % 2 === 0) {
      s = s / 2;
    } else {
      s = 3 * s + 1;
    }
    l++;
  }

  if (l > length) {
    length = l;
    num = i;
  }
}

console.log(num);

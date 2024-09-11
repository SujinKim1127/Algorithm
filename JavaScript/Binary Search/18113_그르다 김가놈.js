const input = require("fs")
  .readFileSync(
    process.platform === "linux"
      ? "/dev/stdin"
      : "JavaScript/Binary Search/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const [n, k, m] = input[0].split(" ").map((v) => +v);
const arr = input.slice(1).map((v) => +v);

const left = [];
for (let i = 0; i < arr.length; i++) {
  if (arr[i] > 2 * k) {
    left.push(Number(arr[i] - 2 * k));
  } else if (arr[i] > k && arr[i] < 2 * k) {
    left.push(Number((arr[i] = arr[i] - k)));
  }
}
if (left.length === 0) console.log(-1);
else {
  let start = 1;
  let end = Math.max(...left);
  let p = -1;
  while (start <= end) {
    let min = Math.floor((start + end) / 2);
    let count = 0;
    for (let i = 0; i < left.length; i++) {
      count += Math.floor(left[i] / min);
    }
    if (count >= m) {
      start = min + 1;
      p = min;
    } else {
      end = min - 1;
    }
  }

  console.log(p);
}

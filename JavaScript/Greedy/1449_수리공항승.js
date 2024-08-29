const input = require("fs")
  .readFileSync(
    process.platform === "linux" ? "/dev/stdin" : "JavaScript/Greedy/input.txt"
  )
  .toString()
  .trim()
  .split("\n");

const [n, l] = input[0].split(" ").map((v) => +v);
const arr = input[1]
  .split(" ")
  .map(Number)
  .sort((pre, cur) => pre - cur);

let result = 1;
let left = +arr[0] - 0.5;

for (let i = 0; i < n; i++) {
  if (left + l < +arr[i]) {
    left = +arr[i] - 0.5;
    result += 1;
  }
}

console.log(result);

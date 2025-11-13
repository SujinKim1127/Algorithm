const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);

const items = input.slice(1).map((line) => {
  const [w, v] = line.split(" ").map(Number);
  return { w, v };
});

let dp = Array(K + 1).fill(0);

items.forEach(({ w, v }) => {
  for (let weight = K; weight >= w; weight--) {
    dp[weight] = Math.max(dp[weight], dp[weight - w] + v);
  }
});

console.log(dp[K]);

const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const arr = [];

rl.on("line", function (line) {
  arr.push(line.trim().split(" "));
}).on("close", function () {
  for (let i = 0; i < 3; i++) {
    arr.push([arr[0][i], arr[1][i], arr[2][i]]);
  }
  let ans = Number.MAX_SAFE_INTEGER;
  for (let i = 0; i < arr.length; i++) {
    for (let i = 0; i < arr.length; i++) {
      ans = Math.min(ans, Math.max(...arr[i]) - Math.min(...arr[i]));
    }
  }
  console.log(ans);
  process.exit();
});

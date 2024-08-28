const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
const [n, m] = input[0].split(" ").map((v) => +v);
const arr = input.slice(1).map((line) => line.split(" ").map(Number));

const findNumberTwo = () => {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (arr[i][j] === 2) return [i, j];
    }
  }
};

const dx = [-1, 1, 0, 0];
const dy = [0, 0, 1, -1];

const dist = new Array(n).fill().map(() => new Array(m).fill(-1));
const start = findNumberTwo();
const [sx, sy] = start;
dist[sx][sy] = 0;

const BFS = (ax, ay) => {
  let queue = [[ax, ay]];

  while (queue.length) {
    const [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];

      if (
        nx >= 0 &&
        nx < n &&
        ny >= 0 &&
        ny < m &&
        arr[nx][ny] !== 0 &&
        dist[nx][ny] === -1
      ) {
        queue.push([nx, ny]);
        dist[nx][ny] = dist[x][y] + 1;
      }
    }
  }
  return dist;
};

const result = BFS(sx, sy);

for (let i = 0; i < n; i++) {
  let line = "";
  for (let j = 0; j < m; j++) {
    if (arr[i][j] === 0) line += "0 ";
    else line += `${result[i][j]} `;
  }
  console.log(line.trim());
}

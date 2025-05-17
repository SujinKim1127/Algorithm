function solution(maps) {
  var answer = 1;
  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, 1, -1];
  var queue = [[0, 0]];
  const n = maps.length;
  const m = maps[0].length;
  console.log(n, m);
  while (queue.length > 0) {
    const [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      const nx = x + dx[i];
      const ny = y + dy[i];
      if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
        if (maps[nx][ny] === 1) {
          queue.push([nx, ny]);
          maps[nx][ny] = maps[x][y] + 1;
        }
      }
    }
  }

  return maps[n - 1][m - 1] === 1 ? -1 : maps[n - 1][m - 1];
}

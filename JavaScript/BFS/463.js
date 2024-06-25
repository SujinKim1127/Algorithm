/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function (grid) {
  // 주변에 1개랑 붙어있으면 3
  // 주변에 2개랑 붙어있으면 2
  // 주변에 3개 붙어있으면 1
  // 주변에 4개면 0
  const h = grid.length;
  const w = grid[0].length;

  let count = 0;

  for (let r = 0; r < h; r++) {
    for (let c = 0; c < w; c++) {
      if (grid[r][c] === 1) {
        if (r - 1 < 0 || grid[r - 1][c] === 0) count++;
        if (r + 1 === h || grid[r + 1][c] === 0) count++;
        if (c - 1 < 0 || grid[r][c - 1] === 0) count++;
        if (c + 1 === w || grid[r][c + 1] === 0) count++;
      }
    }
  }
  return count;
};

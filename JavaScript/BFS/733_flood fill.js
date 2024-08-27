/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function (image, sr, sc, color) {
  let queue = [];
  const sColor = image[sr][sc];
  const length = image.length * image[0].length;
  let counter = 0;

  queue.push([sr, sc]);

  const dx = [-1, 1, 0, 0];
  const dy = [0, 0, -1, 1];

  while (queue.length > 0) {
    if (counter > length) {
      break;
    }
    counter++;
    let [x, y] = queue.shift();

    image[x][y] = color;

    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];
      if (image[nx]) {
        if (image[nx][ny] === sColor) {
          queue.push([nx, ny]);
        }
      }
    }
  }

  return image;
};

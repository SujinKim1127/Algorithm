function solution(triangle) {
  var answer = 0;
  for (let x = 1; x < triangle.length; x++) {
    for (let y = 0; y < triangle[x].length; y++) {
      if (y === 0) {
        triangle[x][y] += triangle[x - 1][y];
      } else if (y === triangle[x].length - 1) {
        triangle[x][y] += triangle[x - 1][y - 1];
      } else {
        triangle[x][y] += Math.max(triangle[x - 1][y], triangle[x - 1][y - 1]);
      }
    }
  }
  // flat으로 하는 방식
  answer = Math.max(...triangle.flat());

  // reduce로 하는 방식
  answer = triangle.reduce((max, row) => {
    // console.log("max", max, "row", row)
    return Math.max(
      max,
      row.reduce((a, b) => {
        // console.log(`acc=${a}, cur=${b}`);
        return Math.max(a, b);
      })
    );
  }, -Infinity);
  return answer;
}

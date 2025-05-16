function solution(brown, yellow) {
  var answer = [];
  const total = brown + yellow;
  for (let height = 3; height <= Math.sqrt(total); height++) {
    const width = total / height;
    if (
      Number.isInteger(width) &&
      width >= height &&
      (width - 2) * (height - 2) === yellow
    ) {
      return [width, height];
    }
  }
}

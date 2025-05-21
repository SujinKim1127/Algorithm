function solution(distance, rocks, n) {
  var answer = 0;

  var start = 0;
  var end = distance;

  rocks.sort((a, b) => a - b);
  rocks.push(distance);

  while (start <= end) {
    var cnt = 0;
    var before = 0;
    const mid = Math.floor((start + end) / 2);

    for (let i = 0; i < rocks.length; i++) {
      const space = rocks[i] - before;
      if (mid > space) {
        cnt += 1;
      } else {
        console.log(mid, rocks[i]);
        // 작은 징검다리는 삭제해버리는 코드!!
        before = rocks[i];
      }
    }

    if (cnt > n) {
      end = mid - 1;
    } else {
      answer = mid;
      start = mid + 1;
    }
  }
  return answer;
}

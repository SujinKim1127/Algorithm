function solution(n, times) {
  var low = 1;
  var high = Math.max(...times) * n;
  while (low < high) {
    var mid = Math.floor((low + high) / 2);
    var people = 0;
    for (const time of times) {
      people += Math.floor(mid / time);
    }
    console.log(mid, people);
    if (people >= n) {
      high = mid;
    } else {
      low = mid + 1;
    }
  }
  return low;
}

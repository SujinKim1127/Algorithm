/**
 * @param {string[]} nums
 * @param {string} target
 * @return {number}
 */
var numOfPairs = function (nums, target) {
  const counter = nums.reduce((acc, cur) => {
    acc[cur] = (acc[cur] || 0) + 1;
    return acc;
  }, {});

  var ans = 0;
  var n = target.length;

  for (let i = 1; i < n; i++) {
    const left = target.slice(0, i);
    const right = target.slice(i);

    if (!counter.hasOwnProperty(left) || !counter.hasOwnProperty(right))
      continue;

    if (left === right) {
      var c = counter[left];
      ans += c * (c - 1);
    } else {
      ans += counter[left] * counter[right];
    }
  }
  return ans;
};

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

/**
 * @param {string[]} nums
 * @param {string} target
 * @return {number}
 */
var numOfPairs = function (nums, target) {
  let count = 0,
    m = target.length;
  let dict = new Map();

  for (let num of nums) {
    let n = num.length;
    if (n >= m) continue;
    // slice 앞부분
    if (target.slice(0, n) === num) count += dict.get(target.slice(n)) || 0;
    // slice 뒷부분
    if (target.slice(m - n) === num)
      count += dict.get(target.slice(0, m - n)) || 0;

    dict.set(num, (dict.get(num) || 0) + 1);

    // console.log(dict)
  }

  return count;
};

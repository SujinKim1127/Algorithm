/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  let arr = [0, 1, 2];
  while (n >= arr.length) {
    const len = arr.length;
    arr.push(arr[len - 1] + arr[len - 2]);
  }
  return arr[n];
};

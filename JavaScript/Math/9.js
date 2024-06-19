/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  const arr = x.toString().split("");
  const reverse = Number([...arr].reverse().join(""));
  if (x === reverse) return true;
  else return false;
};

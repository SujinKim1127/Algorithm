/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  for (let i = 0; i < s.length; i++) {
    let first = s.indexOf(s[i]);
    let last = s.lastIndexOf(s[i]);

    if (first === last) return i;
  }
  return -1;
};

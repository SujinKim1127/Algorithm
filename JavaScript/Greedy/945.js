/**
 * @param {number[]} nums
 * @return {number}
 */
var minIncrementForUnique = function (nums) {
  nums.sort((a, b) => a - b);
  let cnt = 0;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i] <= nums[i - 1]) {
      let increment = nums[i - 1] - nums[i] + 1;
      nums[i] += increment;
      cnt += increment;
    }
  }
  return cnt;
};

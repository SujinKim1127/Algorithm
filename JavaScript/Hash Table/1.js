/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let hashMap = {};
  for (let i = 0; i < nums.length; i++) {
    const gap = target - nums[i];
    if (gap in hashMap) {
      const idx = hashMap[gap];
      return [i, idx];
    }
    hashMap[nums[i]] = i;
  }
};

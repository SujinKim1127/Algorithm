/**
 * 두 개의 배열(base, sample)을 입력받아 sample이 base의 부분집합인지 여부를 리턴해야한다
 */
                        // 1 2 3 4 5    3 5
 const isSubsetOf = function (base, sample) {
    // 각 배열 정렬하기: O(N * logN)
    base.sort((a, b) => a - b);
    sample.sort((a, b) => a - b);
  
    const findItemInSortedArr = (item, arr, from) => {
        // 맨처음 시작은 0으로 
      for (let i = from; i < arr.length; i++) {
        // 같은 아이템이 있으면 i번째 배열부터 다시 비교
        if (item === arr[i]) return i;
        else if (item < arr[i]) return -1;
      }
      return -1;
    };
  
    let baseIdx = 0;        // 시작은 0
    for (let i = 0; i < sample.length; i++) {
      baseIdx = findItemInSortedArr(sample[i], base, baseIdx);
      if (baseIdx === -1) return false;
    }
    return true;
};
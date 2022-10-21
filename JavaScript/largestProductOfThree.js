/**
 * 정수를 요소로 가지는 배열을 입력받아 3개의 요소를
 * 곱해 나올 수 있는 최대값을 리턴
 */

 const largestProductOfThree_short = function (arr) {
    var srt = arr.sort(function(a,b) {return a - b});
    var lgth = arr.length;
    var head = srt[0] * srt[1] * srt[lgth-1];  // 음수일수도 있으므로
    var tail = srt[lgth - 1] * srt[lgth - 2] * srt[lgth - 3];   // 맨마지막 3개
    return Math.max(head, tail);
  };
  

const largestProductOfThree = function (arr) {
    var max = arr[0] * arr[1] * arr[2];
    // 길이만큼 for문 돌리고
    // 3번만 곱하는데
    // 값이 가장 큰걸 업데이트 해주는...
    for(let x = 0; x < arr.length; x++){
      for(let y = 1 + x; y < arr.length; y++){
        for(let z = 2 + x; z < arr.length; z++){
          if(max < arr[x] * arr[y] * arr[z] && x !== y && y !== z && x !== z) {
            max = arr[x] * arr[y] * arr[z];
          }
        }
      }
    }
    return max;
  };
  
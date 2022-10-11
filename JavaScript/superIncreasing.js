/* 
수를 요소로 갖는 배열을 입력받아 각 요소들이 그 이전의
요소들의 합보다 큰지 여부를 리턴하기
*/

function superIncreasing(arr) {
    var sum = 0;
    for(let i = 1; i < arr.length; i++){
      sum += arr[i-1];
      if(sum >= arr[i]) return false;
    }
    return true;
  }
  
/*
문자열을 요소로 갖는 배열을 입력받아 문자열을
세로로 읽었을때의 문자열을 리턴
*/


function readVertically(arr) {
    var cnt = 0;
    var max = arr[0];
    // 가장 길이가 긴 배열의 값을 먼저 구해주고
    for(let i = 1; i < arr.length; i++){
      if(max.length < arr[i].length) max = arr[i];
    }
    var str = "";
    // max값 만큼 for문을 돌린다
    for(let i = 0; i < max.length; i++){
      for(let j = 0; j < arr.length; j++){
        if(arr[j][i] !== undefined) str += arr[j][i]
      }
    }
    return str;
  }
  
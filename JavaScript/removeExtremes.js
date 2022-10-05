/**
 * 문자열을 요소로 갖는 배열을 입력받아 가장 짧은 문자열과
 * 가장 긴 문자열을 제거한 배열 리턴하기
 */

function removeExtremes(arr) {
    var short = arr[0];
    var sidx = 0;
    var long = arr[0];
    var lidx = 0;
    for(let i = 1; i < arr.length; i++){
      if(short.length >= arr[i].length){
        short = arr[i];
        sidx = i;
      }
      if(long.length <= arr[i].length){
        long = arr[i];
        ldx = i;
      }
    }
    if(sidx > ldx){
      arr.splice(sidx,1);
      arr.splice(ldx, 1)
    }
    else if(sidx < ldx){
      arr.splice(ldx, 1)
      arr.splice(sidx,1);
    }
    else{
      arr.splice(ldx, 1);
    }
  
    return arr;
  }
  
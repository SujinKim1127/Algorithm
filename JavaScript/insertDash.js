/**
 * 문자열을 입력받아 연속된 한자리 홀수 숫자 사이에 
 * '-'를 추가한 문자열을 리턴
 */

 function insertDash(str) {
    var arr = str.split('');
    for(let i = 1; i < arr.length; i++){
      if(arr[i-1] % 2 === 1 && arr[i] % 2 ===1) arr.splice(i,0,'-');
    }
    return arr.join('')
  }
  
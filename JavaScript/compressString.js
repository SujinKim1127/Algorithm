/**
 * 문자열을 입력받아 연속되는 문자가 있을 경우
 * 연속 구간을 반복되는 수와 문자로 조합한 형태로 압축한
 * 문자열을 리턴하기
 */

function compressString(str) {
    if(str.length === 0) return '';
    var cnt = 1;
    var result = '';
    str += ' ';
    var before = str[0];
    for(let i = 1; i < str.length; i++){
      if(str[i] === str[i-1]) {
        cnt++
      }
      else{
        if (cnt > 2) {
          result += cnt + str[i-1]
        }
        else result += str[i-1].repeat(cnt)
          cnt = 1
      }    
  
    }
  
  
    return result;
  }
  
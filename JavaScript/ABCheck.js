/**
 * 문자열을 입력받아 문자열 내에 아래 중 하나가 존재하는 여부 리턴
 * a로 시작해서 b로 끝나는 길이 5의 문자열
 * b로 시작해서 a로 끝나는 길이 5의 문자열
 */

function ABCheck(str) {
    var str = str.toLowerCase();        // 대소문자 구분없이
    for(let i = 4; i < str.length; i++){
      if(str[i] === 'a' && str[i-4] === 'b' ||    // b로 시작해서 a로 끝나는 
      str[i] === 'b' && str[i-4] === 'a'){      // a로 시작해서 b로 끝나는
        return true;
      }
    }
    return false
  }
  
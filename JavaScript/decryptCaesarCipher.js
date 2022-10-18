/**
 * 암호화된 문자열과 암호화 키를 입력받아 복호화된 문자열 리턴
 * 카이사르 암호는 평문을 암호키 개수만큼 오른쪽으로 평행이동시켜
 * 암호화한다. 복호화는 암호화된 문자열을 원래의 평문으로 복원하는 것
 */

function decryptCaesarCipher(str, secret) {
    var alpha = 'abcdefghijklmnopqrstuvwxyz';
    var result = '';
    for(let i = 0; i < str.length; i++){
      if(str[i] === ' ') result += ' ';
      else{
        var idx = alpha.indexOf(str[i]) - secret;
        idx = (idx + alpha.length) % alpha.length
        result += alpha[idx];
      }
    }
    return result;
  }
  
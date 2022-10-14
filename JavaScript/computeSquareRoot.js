/**
 * 수를 입력받아 제곱근 값을 소수점 두 자리까지 리턴하기
 * 단, Math.sqrt()는 사용하지 않는다.
 */


function computeSquareRoot(num) {
    var close = num / 2;
    while((close ** 2) !== num){
      if(Number((close ** 2).toFixed(2)) === num) break;
      close = (close + num / close) / 2;
    }
    return Number(close.toFixed(2))
  }
  
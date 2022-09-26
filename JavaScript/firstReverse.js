/*
        문자열을 입력받아 순서가 뒤집힌 문자열 리턴하기
 */

function firstReverse(str) {
    // 먼저 split으로 배열을 만들어주고
    // 배열을 뒤집는 reverse()
    // 배열을 다시 합치는 join
    return str.split("").reverse().join("");
  }
  
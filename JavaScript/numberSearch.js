
/**
 * 문자열을 입력받아 문자열에서 숫자를 모두 찾아 더한 후
 * 해당 값을 (숫자, 공백 제외) 문자열의 길이로 나눈값을
 * 정수로 반올림하여 리턴
 */
function numberSearch(str) {
    if(str === '') return 0;
    var num = str.match(/\d+/g).map(Number);
    var sum = num.reduce( (prev, curr) => prev + curr );
    var length = str.split(' ').join('').length - num.length;
    return Math.round(Number(sum)/length)
  }
  
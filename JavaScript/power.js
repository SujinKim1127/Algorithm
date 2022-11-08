/**
 * 두 수를 입력받아 거듭제곱 리턴하기
 * 실제 계산 결과를 94906249 로 나눈 나머지 리턴하기
 * Math.pow, 거듭제곱 연산자 사용 금지
 * 시간복잡도 O(logN) 만족하기
 */

 function power(base, exponent) {

    if (exponent === 0) return 1;
  
    const half = parseInt(exponent / 2);
    const temp = power(base, half);
    const result = (temp * temp) % 94906249;
  
    if (exponent % 2 === 1) return (base * result) % 94906249;
    else return result;
  
}
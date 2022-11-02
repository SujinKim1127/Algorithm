/**
 * 세로 길이 2, 가로 길이 n인 2*n 보드가 있다
 * 2 * 1 크기의 타일을 가지고 이 보드를 채우는 모든 경우의 수 리턴하기
 */

// 피보나치 O(n)을 활용하여 적용
 let tiling = function (n) {
    const memo = [0, 1, 2];
    const aux = (n) => {
      if(memo[n] !== undefined) return memo[n];
      memo[n] = aux(n-1) + aux(n-2)
      return memo[n]
    }
    
    return aux(n);
  
  };
  
// dynamic with tabulation: O(N)
// tabulation: 데이터를 테이블에 정리하면서 bottom-up 방식으로 해결하는 것
let tiling_2 = function (n) {
  const memo = [0, 1, 2];
  if (n <= 2) return memo[n];
  for(let size = 3; size <= n; size++){
    memo[size] = memo[size - 1] + memo[size - 2]
  }
  return memo[n]
}

// dynamic with slicing window: O(N)
// slicing window: 필요한 최소한의 데이터만 활용
// n의 문제에 대한 해결을 위해 필요한 데이터는 오직 2개뿐이다
let tiling_3 = function (n) {
  let first = 1, second = 2;
  if(n <= 2) return n;
  for(let size = 3; size <= n; size++){
    // 앞의 두 수를 더하여 다음 수 구하기
    const next = first + second;

    // 다음 문제로 넘어가기 위해 필요한 2개의 데이터 순서 정리
    fisrt = second;
    second = next;
  }
  return second;
}
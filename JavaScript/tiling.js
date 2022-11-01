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
  
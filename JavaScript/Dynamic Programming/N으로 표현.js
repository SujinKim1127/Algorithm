function solution(N, number) {
  if (N === number) return 1;
  let dp = Array.from({ length: 9 }, () => new Set());

  // 붙여쓴 숫자 만들기
  for (let i = 1; i <= 8; i++) {
    dp[i].add(Number(String(N).repeat(i)));
  }

  for (let i = 1; i <= 8; i++) {
    // i를 두개로 만들기
    for (let j = 1; j < i; j++) {
      for (let a of dp[j]) {
        for (let b of dp[i - j]) {
          dp[i].add(a + b);
          dp[i].add(a - b);
          dp[i].add(a * b);
          if (b !== 0) dp[i].add(Math.floor(a / b));
        }
      }
    }
    if (dp[i].has(number)) return i;
  }

  return -1;
}

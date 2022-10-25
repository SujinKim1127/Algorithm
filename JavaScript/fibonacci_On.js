function fibonacci(n) {
    const memo = [0, 1];
    const aux = (n) => {
    // 이미 저장해둔 값이 있으면 그 값을 리턴하기
    if (memo[n] !== undefined) return memo[n];
    // 저장해둔 값이 없으면 메모에 적기
    memo[n] = aux(n - 1) + aux(n - 2);
    return memo[n];
    };
    return aux(n);
}

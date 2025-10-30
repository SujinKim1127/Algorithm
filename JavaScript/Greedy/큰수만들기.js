function solution(number, k) {
  const stack = [];

  for (let num of number) {
    // 스택의 마지막 값보다 현재 값이 크면 pop()
    while (k > 0 && stack.length && stack[stack.length - 1] < num) {
      stack.pop();
      k--;
    }
    stack.push(num); // 현재 숫자 추가
  }

  // 아직 제거할 숫자가 남아있는지
  stack.splice(stack.length - k, k);

  return stack.join("");
}

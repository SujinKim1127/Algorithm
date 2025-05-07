function solution(progresses, speeds) {
  var remain = progresses.map((progress, idx) =>
    Math.ceil((100 - progress) / speeds[idx])
  );
  var idx = 0;
  var answer = [];

  var stack = [];
  var count = 1;
  var max = remain[0];
  for (let i = 1; i < progresses.length; i++) {
    if (max >= remain[i]) {
      count += 1;
    } else {
      answer.push(count);
      max = remain[i];
      count = 1;
    }
  }
  answer.push(count);
  return answer;
}

// 다음작업이 이전보다 빠르게 완성되면 다음꺼 같이 배포

// 5[1] 10 1 1[3] 20 1[2]
// 7 3[2] 9[1]

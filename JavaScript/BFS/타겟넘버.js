2;
3;
4;
5;
6;
7;
8;
9;
10;
11;
12;
13;
14;
15;
16;
17;
18;
function solution(numbers, target) {
  var answer = 0;
  var calculate = [0];
  for (let i = 0; i < numbers.length; i++) {
    var temp = [];
    for (let j = 0; j < calculate.length; j++) {
      temp.push(calculate[j] + numbers[i]);
      temp.push(calculate[j] - numbers[i]);
    }
    calculate = temp;
  }

  for (let i = 0; i < calculate.length; i++) {
    if (calculate[i] === target) answer += 1;
  }
  return answer;
}

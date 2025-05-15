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
19;
20;
21;
22;
23;
24;
25;
function solution(clothes) {
  var answer = 0;
  var hashMap = new Map();
  for (let i = 0; i < clothes.length; i++) {
    const [item, type] = clothes[i];
    if (hashMap.has(type)) {
      hashMap.get(type).push(item);
    } else {
      hashMap.set(type, [item]);
    }
  }

  console.log(hashMap);

  hashMap.forEach((value, key) => {
    const count = value.length;
    if (answer === 0) {
      answer = count + 1;
    } else {
      answer = answer * (count + 1);
    }
  });
  return answer - 1;
}

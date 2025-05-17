function solution(phone_book) {
  var answer = true;
  phone_book.sort();
  const len = phone_book.length;
  for (let i = 0; i < len - 1; i++) {
    if (phone_book[i + 1].startsWith(phone_book[i])) return false;
  }
  return answer;
}

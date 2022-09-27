// case 1
function letterCapitalize(str) {
    var arr = str.split(' ');
    for(let i = 0; i < arr.length ; i++) {
      // 배열에 공백이 있을 경우
      if(arr[i].length !== 0){
        var sp = arr[i].split('');   // 문자열 배열로 한번 더 자르고
        // 자른거 첫글자만 대문자로 바꾸기
        sp.splice(0,1,sp[0].toUpperCase())
        arr[i] = sp.join("")
      }
    }
    arr = arr.join(" ")
    return arr
}

// case 2
function letterCapitalize(str) {
    var arr = str.split(' ');
    for(let i = 0; i < arr.length ; i++) {
      // 배열에 공백이 있을 경우
      if(arr[i].length > 0){        // 처음을 제외한 나머지 글자만 반환
        arr[i] = arr[i][0].toUpperCase() + arr[i].substr(1);
      }
    }
    arr = arr.join(" ")
    return arr
}


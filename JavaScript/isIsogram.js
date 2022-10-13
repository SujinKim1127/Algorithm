/*
문자열을 입력받아 아이소그램인지 여부를 리턴
아이소그램: 각 알파벳을 한번씩만 이용해서 만든 단어나 문구
*/ 

function isIsogram(str) {
    str = str.toLowerCase();
    var arr = str.split('');
    for(let i = 0; i < str.length; i++){
      if(str.indexOf(str[i]) !== i) return false
    }
    return true;
  }
  
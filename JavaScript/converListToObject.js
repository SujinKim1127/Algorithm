/**
 * 입력한 배열을 객체로 만들기
 * 단, 중복되는 키의 경우, 초기의 값을 사용한다.
 * 빈 배열은 빈 객체 리턴
 */

function convertListToObject(arr) {
    var obj = {};
    for(let i = 0;i < arr.length; i++){
      if(arr[i].length > 0 && !Object.keys(obj).includes(arr[i][0])){ // obj[arr[i][0]] === undefined
        obj[arr[i][0]] = arr[i][1]
      }
    }
    return obj
  }
  
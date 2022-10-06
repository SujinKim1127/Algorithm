/**
 * 2차원 배열(배열을 요소로 갖는 배열)을 입력받아
 * 'B' 의 위치정보를 요소로 가지는 배열 리턴하기
 */

function findBugInApples(arr) {
    for(let i = 0; i < arr.length; i++){ // 행
      for(let j = 0; j < arr[i].length; j++){
        if(arr[i][j] === 'B'){
          return [i,j];
        }
      }  
    }
  }
  
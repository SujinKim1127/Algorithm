const swap = function (idx1, idx2, arr) {
    [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]]
  }
  
  const bubbleSort = function (arr) {
    // TODO: 여기에 코드를 작성합니다.
    for(let i = 0; i < arr.length; i++){
      let cnt = 0;    // swap된 횟수 구하기
      
      // 매반복마다 i번째로 큰수가 i번째에 위치한다
      // 이미 정렬된 값은 비교할 필요 없으므로 arr.length - 1 - i
      for(let j = 0; j < arr.length - 1 - i; j++){
        if(arr[j] > arr[j+1]){
          cnt++;
          swap(j, j+1, arr)
        }
      }
  
      // swap되지 않으면 정렬된 상태
      if(cnt === 0) break;
    }
    return arr
  };
  
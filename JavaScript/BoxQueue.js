function paveBox(boxes) {
    let max = boxes[0]
    let result = [1];
    let idx = 0;        // max값이 갱신될때 필요
    for(let i = 1; i < boxes.length; i++){
      if(boxes[i] > max) {  // 최대값 갱신
        max = boxes[i]
        idx++;
        result.push(1)
      }
      else if(max >= boxes[i]){
        result[idx]++
      }
    }
    return Math.max(...result)
  }
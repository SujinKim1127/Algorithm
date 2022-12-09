function boardGame(board, operation) {
    operation = operation.split('')
    if(operation[0] === 'U') return 'OUT';
    let pnt = 0;
    let now = [0, 0];
    while(operation.length > 0){
      let pos = operation.shift();
      switch(pos){
        case 'R' :
          now[1] += 1;
          pnt += board[ now[0] ][ now[1] ]
          break;
        case 'L' :
          now[1] -= 1;
          pnt += board[ now[0] ][ now[1] ]
          break;
        case 'U' :
          now[0] -= 1;
          pnt += board[ now[0] ][ now[1] ]
          break;
        case 'D' :
          now[0] += 1;
          pnt += board[ now[0] ][ now[1] ]
          break;
  
      }
      console.log(now)
  
    }
    return pnt;
    // 오른쪽은 [][+1]
    // 왼쪽은 [-1][]
    // 아래는 [+1][]
    // 위는 [-1][]
  };
  
  const board3 = 
  [
    [0, 0, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0],
  ];
    const output2 = boardGame(board3, 'RRDLLD');
  console.log(output2); // 'OUT'
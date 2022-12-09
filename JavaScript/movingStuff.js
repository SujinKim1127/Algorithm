function movingStuff(stuff, limit) {

    let cnt = 0;
    // 내림차순으로 정렬하고 
    stuff.sort(function(a, b)  {
    return b - a;
    });
    while(stuff.length > 0){
        // 앞에꺼 빼고
      let fst = stuff.shift();
  
      // 앞값이랑 나머지랑 비교
      for(let i = 0; i < stuff.length; i++){
        // 찾으면 cnt++ 하고 해당 값 빼오기
        if(fst + stuff[i] <= limit){
          stuff.splice(i,1);
          console.log("splice ", fst, '+', stuff[i])
          break;
        }
      }
      cnt++;
    }
    return cnt;
  }
  
  
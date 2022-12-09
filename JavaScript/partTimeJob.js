function partTimeJob(k) {
    let cnt = 0;
    const coins = [500,100,50,10,5,1];
  
    for(let i = 0; i < coins.length; i++){
        cnt += Math.floor(k/coins[i])

        k = k % coins[i]
        console.log(k, cnt);
    }
  
  }
  partTimeJob(4972)
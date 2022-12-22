function rockPaperScissors (n) {
    let rps = ['rock', 'paper', 'scissors'];
    const recur = function(rps, selectNum){
        const result = [];
        if(selectNum === 1) return rps.map(el => [el]);

        rps.forEach((fixed, idx, rps) => {
            const permutations = recur(rps, selectNum - 1);

            const attached = permutations.map((el) => [fixed, ...el])
            result.push(...attached);
        })
        return result;

    }

    return recur(rps, n || 3);
  };


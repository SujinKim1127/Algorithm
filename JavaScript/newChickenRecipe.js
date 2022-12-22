function newChickenRecipe(stuffArr, choiceNum) {
    stuffArr = stuffArr.filter(el => !String(el).includes('000'));

    const recur = function (arr, selectNum) {
        const result = [];
        if(selectNum === 1) return arr.map(el => [el]);

        arr.forEach((fixed, idx, orgin) => {
            const rest = [...orgin.slice(0, idx), ...orgin.slice(idx+1)]
            const permutations = recur(rest, selectNum - 1);

            const attached = permutations.map((el) => [fixed, ...el])
            result.push(...attached);
        });
        return result;
    }
    return recur(stuffArr, choiceNum)
}
  
  const output3 = newChickenRecipe([11, 1, 10, 1111111111, 10000], 4);
console.log(output3)

const output1 = newChickenRecipe([1, 10, 1100, 1111], 2);
console.log(output1);
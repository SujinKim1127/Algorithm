function missHouseMeal(sideDishes) {
    const result = [];

    sideDishes.sort();

    function recur (subset, start) {
        result.push(subset);

        for(let i = start; i < sideDishes.length; i++){
            recur([...subset, sideDishes[i]], i + 1);
        }
    }
    recur([], 0);

    return result;
}

console.log(missHouseMeal(['pasta', 'oysterSoup', 'beefRibs', 'tteokbokki']))
function divideChocolateStick(M, N) {
    let result = [];

    // 유클리드 호제법으로 최대공약수 구하기
    function gcd(a, b) {
        while (b !== 0){
            let r = a % b;
            a = b;
            b = r;
        }
        return a;
    }

    // 최대공약수의 약수 구하기
    const divisors = [];
    for(let i = 1; i <= Math.sqrt(gcd(M,N)); i++){
        if(gcd(M,N) % i === 0){
            divisors.push(i)
            if(gcd(M,N) / i !== i) divisors.push(gcd(M,N) / i)
        }
    }
    divisors.sort((a,b) => a - b)

    for(let num of divisors){
        result.push([num, M / num, N / num])
    }
    return result;
}
let M = 4;
let N = 8;
let output = divideChocolateStick(M, N);
console.log(output);
const calculeFatorial = (n: number) => {
    if (n === 0) {
    return 1
    }
    for (let i = n - 1; i > 0; i--) {
    n *= i;
    }
    return n;
}

const n = 3
const factorial = calculeFatorial(n);
console.log(`O fatorial de ${n} é ${factorial}`)

let num: number[] = []
let x: number = 1
let maior: number=1
let i: number = 0

while(maior<=19){
    x=(Math.random() *99)
    let n = parseInt(x.toString())
    num.push(n)
    i=i+1
    if(maior>n){
        maior=n
    }
}
console.log('O maior numero é:',maior)

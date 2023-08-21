const calculodomes = (valor: number, meses: number = 3, taxa: number = 10) => {
    let resultado = (valor * meses * taxa) / 100
    return resultado 
}

console.log(`R$ ${calculodomes(100.0, 4, 12)}`)
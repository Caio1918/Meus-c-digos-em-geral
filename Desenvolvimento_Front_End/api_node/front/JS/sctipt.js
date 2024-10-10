const protocolo = "http://"
const baseURL = "localhost:3000"
const filmesEndpoint = "/filmes"

async function obterFilmes() {
    const URLCompleta = `${protocolo}${baseURL}${filmesEndpoint}`
    const filmes = (await axios.get(URLCompleta)).data

    let tabela = document.querySelector(".filmes")
    let corpoTabela = tabela.getElementsByTagName("tbody")[0]

    for (let filme of filmes) {

        let linha = corpoTabela.insertRow(0)
        let celulaTitulo = linha.insertCell(0)
        let celulaSinopse = linha.insertCell(1)

        celulaTitulo.innerHTML = filme.titulo
        celulaSinopse.innerHTML = filme.sinopse
    }
}

async function cadastrarFilme() {

    // Contrói a URL completa
    const URLCompleta = `${protocolo}${baseURL}${filmesEndpoint}`

    // Pega os inputs que contém os valores que o usuário digitou
    let tituloInput = document.querySelector("#tituloInput")
    let sinopseInput = document.querySelector("#sinopseInput")

    // Pega os valores digitados pelo usuário
    let titulo = tituloInput.value
    let sinopse = sinopseInput.value

    //  Somente adiciona se o usuário tiver digitado os dois valores
    if (titulo && sinopse) {

        // Limpa os campos que o usuário digitou
        tituloInput.value = ""
        sinopseInput.value = ""

        // Envia os dados ao servidor (back end)
        const filmes = (await axios.post(URLCompleta, { titulo, sinopse })).data

        // Limpa a tabela para preenchê-la com a coleção nova, atualizada
        let tabela = document.querySelector(".filmes")
        let corpoTabela = tabela.getElementsByTagName("tbody")[0]
        corpoTabela.innerHTML = ""

        for (let filme of filmes) {

            let linha = corpoTabela.insertRow(0)

            let celulaTitulo = linha.insertCell(0)
            let celulaSinopse = linha.insertCell(1)

            celulaTitulo.innerHTML = filme.titulo
            celulaSinopse.innerHTML = filme.sinopse
        }
    }

    // Senão, exibe o alerta por até 2 segundos
    else {
        let alert = document.querySelector('.alert')
        alert.classList.add('show')
        alert.classList.remove('d-none')
        setTimeout(() => {
            alert.classList.remove('show')
            alert.classList.add('d-none')
        }, 2000)
    }
}
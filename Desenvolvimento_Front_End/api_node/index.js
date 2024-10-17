const express = require ("express")
const cors = require ("cors")
const app = express()

app.use(express.json())
app.use(cors())

let filmes = [
    {
      titulo: "Forrest Gump - Contador de Histórias",
      sinopse: "Quarenta anos da história dos Estados Unidos, vistos pelos olhos de Forrest Gump (Tom Hanks), um rapaz com QI abaixo da média e boas intenções." ,
      ano: 1994,
      classificacao: "A"  
    },
    {
      titulo: "Um Sonho de Liberdade",
      sinopse: "Em 1946, Andy Dufresne (Tim Robbins), um jovem e bem sucedido banqueiro, tem a sua vida radicalmente modificada ao ser condenado por um crime quenunca cometeu, o homicídio de sua esposa e do amante dela",
      ano: 1994,
      classificacao: "A"
    }
    
]

app.get("/filmes", (req, res) => {
  res.json(filmes)
})

app.post("/filmes", (req, res) => {
  //Obtém os dados enviados pelo cliente
  const titulo = req.body.titulo
  const sinopse = req.body.sinopse
  //Monta um objeto agrupando os dados. Ele representa um novo filme
  const filme = {titulo: titulo, sinopse: sinopse}
  //Adiciona o novo filme à base
  filmes.push(filme)
  //Responde ao cliente. Aqui, optamos por devolver a base interira ao clientne.
  res.json(filmes)
})

//GET http://localhost:3000/hey
app.get("/hey", (req, res) => {
    res.send("hey")
})

app.listen(3000, () => console.log("up and running"))


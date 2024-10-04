const express = require ("express")
const app = express()
app.use(express.json())

//GET http://localhost:3000/hey
app.get("/hey", (req, res) => {
    res.send("hey")
})

app.listen(3000, () => console.log("up and running"))


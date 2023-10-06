import express from "express";

const app = express();

app.use(express.json())

const livros = [
    {id: 1, "Titulo": "Senhor dos Aneis"},
    {id: 2, "Titulo": "O Hobiit"}
]

app.get('/', (req, res) => {
    res.status(200).send('Curso de Node');
})


app.get('/livros', (req, res) => {
    res.status(200).json(livros);
})

app.post('/livros', (req, res) => {
    livros.push(req.body);
    res.status(201).send('Livro foi cadastrado com sucesso.')
})

app.put('/livros/:id', (req, res) => {
    let index = buscaLivro(req.params.id);
    livros[index].Titulo = req.body.Titulo;
    res.json(livros);
})

function buscaLivro(id) {
    return livros.findIndex(livro => livro.id == id)
}
export default app 
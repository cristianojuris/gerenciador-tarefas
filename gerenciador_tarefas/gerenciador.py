from fastapi import FastAPI
TAREFAS  = [
    {"id": 1, "titulo": "Cristiano"},
    {"id": 2, "titulo": "Araujo"}
]

app = FastAPI()


@app.get('/tarefas')
def listar():
    return TAREFAS
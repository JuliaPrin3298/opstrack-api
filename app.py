from flask import Flask
app = Flask(__name__)
@app.route('/')
#def status():
#    return{'servico': 'OpsTrackAPI', 'status': 'online'}
# /status — retorna o status do serviço

@app.route("/status")
def status():
    return {
        "status": "online"
    }

@app.route("/tickets")
def tickets():
    return [
        {
            "id": 1,
            "titulo": "Erro no login",
            "status": "aberto"
        },
        {
            "id": 2,
            "titulo": "Problema no pagamento",
            "status": "em andamento"
        },
        {
            "id": 3,
            "titulo": "Atualização de cadastro",
            "status": "fechado"
        }
    ]

@app.route("/sobre")
def sobre():
    return {
        "nome": "Minha API",
        "versao": "1.0.0"
    }


#teste de diff
if __name__ == '__main__':
    app.run(debug=True)

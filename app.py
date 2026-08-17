from flask import Flask
app = Flask(__name__)
@app.route('/')
def status():
    return{'servico': 'OpsTrackAPI', 'status': 'online'}

#teste de diff
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from service import SessaoService

app = Flask(__name__)
service = SessaoService()

@app.route('/')
def index():
    sessoes = service.listar_catalogo()
    return render_template('index.html', sessoes=sessoes)

@app.route('/comprar/<int:sessao_id>', methods=['POST'])
def comprar(sessao_id):
    service.comprar_ingresso(sessao_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
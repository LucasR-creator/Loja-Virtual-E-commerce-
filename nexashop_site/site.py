from flask import Flask, render_template, request, redirect, url_for, flash
from banco import conectar, criar_tabelas

app = Flask(__name__)
app.secret_key = 'desenvolvimento-local-trocar-antes-de-publicar'
criar_tabelas()

@app.get('/')
def inicio():
    with conectar() as conexao:
        conexao.row_factory = __import__('sqlite3').Row
        produtos = [dict(item) for item in conexao.execute('''
            SELECT p.*, ROUND(AVG(a.nota), 1) AS media,
                   COUNT(a.id) AS total_avaliacoes
            FROM produtos p LEFT JOIN avaliacoes a ON a.produto_id = p.id
            GROUP BY p.id ORDER BY p.id DESC
        ''')]
    return render_template('index.html', produtos=produtos)

@app.post('/admin/produtos')
def cadastrar():
    nome = request.form.get('nome', '').strip()
    categoria = request.form.get('categoria', '').strip()
    descricao = request.form.get('descricao', '').strip()
    imagem = request.form.get('imagem', '').strip()
    try:
        preco = float(request.form.get('preco', '').replace(',', '.'))
        estoque = int(request.form.get('estoque', ''))
    except ValueError:
        flash('Preço ou estoque inválido.')
        return redirect(url_for('inicio') + '#admin')
    if not nome or not categoria or not descricao or preco <= 0 or estoque < 0:
        flash('Preencha os dados corretamente.')
        return redirect(url_for('inicio') + '#admin')
    if imagem and not imagem.startswith(('https://', 'http://')):
        flash('A imagem deve ser um endereço http ou https.')
        return redirect(url_for('inicio') + '#admin')
    with conectar() as conexao:
        conexao.execute('''INSERT INTO produtos
            (nome, categoria, descricao, preco, estoque, imagem)
            VALUES (?, ?, ?, ?, ?, ?)''',
            (nome, categoria, descricao, preco, estoque, imagem))
    flash('Produto cadastrado com sucesso!')
    return redirect(url_for('inicio') + '#produtos')

if __name__ == '__main__':
    app.run(debug=True)

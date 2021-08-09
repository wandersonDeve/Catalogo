from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'naosei'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ncsbulqz:2QrPNdtts-s3z6mtlJdXL6dA_DNy93on@kesavan.db.elephantsql.com/ncsbulqz'
db = SQLAlchemy(app)

class Catalogo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    imagem = db.Column(db.String(300), nullable=False)
    descricao = db.Column(db.String(500), nullable=False)
    link = db.Column(db.String(200), nullable=False)
    

    def __init__(self,nome,imagem,descricao,link):
        self.nome = nome
        self.imagem = imagem
        self.descricao = descricao
        self.link = link


@app.route('/')
def index():
    catalogo = Catalogo.query.all()
    return render_template('index.html', catalogo=catalogo)

@app.route('/participantes')
def participantes():
    return render_template('participantes.html')

@app.route('/sinopse/<id>')
def sinopse(id):
    catalogo = Catalogo.query.get(id)
    return render_template('sinopse.html', catalogo=catalogo)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/layout')
def layout():
    catalogo = Catalogo.query.all()
    return render_template('layout.html', catalogo=catalogo)

@app.route('/trailer/<id>')
def trailer(id):
    return render_template('trailer.html')


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        catalogo = Catalogo(
            request.form['nome'],
            request.form['imagem'],
            request.form['descricao'],
            request.form['link'],
        )
        db.session.add(catalogo)
        db.session.commit()
        flash('Catalogo adicionado com sucesso')
        return render_template('adicionar.html')
    return render_template('adicionar.html')

@app.route('/delete/<id>')
def delete(id):
    catalogo = Catalogo.query.get(id)
    db.session.delete(catalogo)
    db.session.commit()
    flash('Projeto apagado com sucesso')
    return redirect('/adicionar')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
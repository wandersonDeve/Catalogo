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

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        catalogo = Catalogo(
            request.form['nome'],
            request.form['imagem'],
            request.form['descricao'],
            request.form['link'],
        )
        db.session.add(catalogo)
        db.session.commit()
        flash('Catalogo Atualizado com sucesso')
        return redirect('/')
    return render_template('adicionar.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
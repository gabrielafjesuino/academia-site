from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/academias')
def academias():
    return render_template('academias.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/imc')
def imc():
    return render_template('imc.html')

@app.route('/verificar', methods=['POST'])  #Define uma rota '/verificar' que aceita apenas requisições POST
def verificar():

    altura = float(request.form['altura'])
    peso = float(request.form['peso'])
    imc = peso / (altura ** 2)
    imc = round(imc, 2)

    if imc < 18.5:
        resultado = "Magreza"
    elif imc >= 18.5 and imc <= 24.99:
        resultado = "Normal"
    elif imc >= 25 and imc <= 29.99:
        resultado = "Sobrepeso"
    elif imc >= 30 and imc <= 34.99:
        resultado = "Obesidade grau I"
    elif imc >= 35 and imc <= 39.99:
        resultado = "Obesidade grau II"
    else:
        resultado = "Obesidade grau III"

    return render_template('imc.html', resultado_python = f'Seu Índice de Massa Corporal (IMC) é: {imc}',  resultado = resultado)
if __name__ == '__main__': #Inicia o servidor Flask em modo de depuração se este script for executado diretamente
    app.run(debug=True)
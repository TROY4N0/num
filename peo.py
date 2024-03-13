from flask import Flask

app = Flask('__name__')

@app.route('/suma/<int:num1>,<int:num2>')
def suma(num1, num2):
        
        resultado  = num1 + num2
        return f'<center><h1>{num1} + {num2} = {resultado}</h1></center>'

@app.route('/resta/<int:num1>,<int:num2>')
def resta(num1, num2):
        
        resultado = num1 - num2
        return f'<center><h1>{num1} - {num2} = {resultado}</h1></center>'

@app.route('/multiplicacion/<int:num1>,<int:num2>')
def multiplicacion(num1, num2):
        
        resultado = num1 * num2
        return f'<center><h1>{num1} * {num2} = {resultado}</h1></center>'

@app.route('/division/<int:num1>,<int:num2>')
def division(num1, num2):
        
        resultado = num1 / num2
        return f'<center><h1>{num1} / {num2} = {resultado}</h1></center>'


@app.route('/')
def angel():
    return '<center><h1>Bienvenido</h1></center>'

if __name__ == '__main__':
    app.run(debug=True)
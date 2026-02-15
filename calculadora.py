from flask import Flask, render_template, request
import os
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        num1_str = request.form.get('num1', '').strip()
        num2_str = request.form.get('num2', '').strip()
        operacao = request.form.get('operacao', '').strip()
        if num2_str and operacao:
            try:
                num1 = float(num1_str)
                num2 = float(num2_str)
                if operacao == '+':
                    resultado = num1 + num2
                elif operacao == '-':
                    resultado = num1 - num2
                elif operacao == '*':
                    resultado = num1 * num2
                elif operacao == '/':
                    if num2 == 0:
                        resultado = 'Erro: Divisão por zero'
                    else:
                        resultado = num1 / num2
                else:
                    resultado = 'Operação inválida'
            except ValueError:
                resultado = 'Entrada inválida'
        elif num1_str:
            try:
                if not all(c.isdigit() or c in '+-*/().' or c.isspace() for c in num1_str):
                    resultado = 'Entrada inválida'
                else:
                    resultado = eval(num1_str)
                    if not isinstance(resultado, (int, float)) or not (-float('inf') < resultado < float('inf')):
                        resultado = 'Erro'
            except ZeroDivisionError:
                resultado = 'Erro: Divisão por zero'
            except:
                resultado = 'Entrada inválida'
    return render_template('index.html', resultado=resultado)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=(os.environ.get('FLASK_DEBUG','0')=='1'))

from typing import Final
from flask import Flask, render_template, request
import requests
from decimal import Decimal

app = Flask(__name__)

def get_coin(moeda1, moeda2, value1, value2):
    url = requests.get(f'https://economia.awesomeapi.com.br/all/{moeda1}-{moeda2}')
    info = url.json()
    final_info = float(info[value1][value2])
    f_coin = float(final_info)
    return f_coin






@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        value = request.form['moeda']
        value2 = request.form['moeda2']
        if value == 'real' and value2 == 'dolar-americano':
            dolar = get_coin('BRL', 'USD', 'BRL', 'high')
            input = request.form['valor']
            final = float(input) * float(dolar)
            return render_template('index.html', moeda=f'US${final:.2f}')

        if value == 'real' and value2 == 'dolar-canadense':
            dolar_canadense = get_coin('CAD', 'BRL', 'CAD', 'high')
            input = request.form['valor']
            final = float(input) / float(dolar_canadense)
            return render_template('index.html', moeda=f'CAD${final:.2f}')

        if value == 'real' and value2 == 'euro':
            euro = get_coin('EUR', 'BRL', 'EUR', 'high')
            input = request.form['valor']
            final = float(input) / float(euro)
            return render_template('index.html', moeda=f'€{final:.2f}')

        if value == 'real' and value2 == 'iene':
            iene = get_coin('JPY', 'BRL', 'JPY', 'high')
            input = request.form['valor']
            final = float(input) / float(iene)
            return render_template('index.html', moeda=f'¥{final:.2f}')

        if value == 'real' and value2 == 'yuan':
            yuan = get_coin('CNY', 'BRL', 'CNY', 'high')
            input = request.form['valor']
            final = float(input) / float(yuan)
            return render_template('index.html', moeda=f'CN¥{final:.2f}')

        if value == 'dolar-americano' and value2 == 'real':
            real = get_coin('BRL', 'USD', 'BRL', 'high')
            input = request.form['valor']
            final = float(input) / float(real)
            return render_template('index.html', moeda=f'R${final:.2f}')

        if value == 'dolar-americano' and value2 == 'dolar-canadense':
            dolar_canadense = get_coin('CAD', 'USD', 'CAD', 'high')
            input = request.form['valor']
            final = float(input) / float(dolar_canadense)
            return render_template('index.html', moeda=f'CAD${final:.2f}')

        if value == 'dolar-americano' and value2 == 'euro':
            euro = get_coin('EUR', 'USD', 'EUR', 'high')
            input = request.form['valor']
            final = float(input) / float(euro)
            return render_template('index.html', moeda=f'€{final:.2f}')

        if value == 'dolar-americano' and value2 == 'iene':
            iene = get_coin('JPY', 'USD', 'JPY', 'high')
            print(iene)
            input = request.form['valor']
            final = float(input) / float(iene) * 100
            return render_template('index.html', moeda=f'¥{final:.2f}')

        if value == 'dolar-americano' and value2 == 'yuan':
            yuan = get_coin('CNY', 'USD', 'CNY', 'high')
            input = request.form['valor']
            final = float(input) / float(yuan)
            return render_template('index.html', moeda=f'{final:.2f}')

        if value == 'dolar-canadense' and value2 == 'dolar-americano':
            dolar_americano = get_coin('CAD', 'USD', 'CAD', 'high')
            input = request.form['valor']
            final = float(input) * float(dolar_americano)
            return render_template('index.html', moeda=f'{final:.2f}')

        if value == 'dolar-canadense' and value2 == 'euro':
            euro = get_coin('CAD', 'EUR', 'CAD', 'high')
            input = request.form['valor']
            final = float(input) * float(euro)
            return render_template('index.html', moeda=f'€{final:.2f}')

        if value == 'dolar-canadense' and value2 == 'iene':
            return render_template('index.html', moeda='Operação indisponível no momento.')

        if value == 'dolar-canadense' and value2 == 'yuan':
            return render_template('index.html', moeda='Operação indisponível no momento.')

        if value == 'euro' and value2 == 'dolar-americano':
            dolar_americano = get_coin('USD', 'EUR', 'USD', 'high')
            input = request.form['valor']
            final = float(input) / float(dolar_americano)
            return render_template('index.html', moeda=f'US${final:.2f}')

        if value == 'euro' and value2 == 'dolar-canadense':
            dolar_canadense = get_coin('CAD', 'EUR', 'CAD', 'high')
            input = request.form['valor']
            final = float(input) / float(dolar_canadense)
            return render_template('index.html', moeda=f'CAD${final:.2f}')

        if value == 'euro' and value2 == 'iene':
            iene = get_coin('JPY', 'EUR', 'JPY', 'high')
            input = request.form['valor']
            final = float(input) / float(iene) * 100
            return render_template('index.html', moeda=f'¥{final:.2f}')

        if value == 'euro' and value2 == 'yuan':
            yuan = get_coin('CNY', 'EUR', 'CNY', 'high')
            input = request.form['valor']
            final = float(input) / float(yuan)
            return render_template('index.html', moeda=f'CN¥{final:.2f}')

        if value == 'euro' and value2 == 'real':
            real = get_coin('BRL', 'EUR', 'BRL', 'high')
            input = request.form['valor']
            final = float(input) / float(real)
            return render_template('index.html', moeda=f'R${final:.2f}')

        if value == 'iene' and value2 == 'dolar-americano':
            dolar_americano = get_coin('JPY', 'USD', 'JPY', 'high')
            input = request.form['valor']
            final = float(input) * float(dolar_americano)
            return render_template('index.html', moeda=f'US${final:.2f}')

        if value == 'iene' and value2 == 'dolar-canadense':
            return render_template('index.html', moeda='Operação indisponível no momento.')

        if value == 'iene' and value2 == 'euro':
            euro = get_coin('JPY', 'EUR', 'JPY', 'high')
            input = request.form['valor']
            final = float(input) * float(euro)
            return render_template('index.html', moeda=f'US${final:.2f}')


        if value == 'iene' and value2 == 'euro':
            euro = get_coin('JPY', 'EUR', 'JPY', 'high')
            input = request.form['valor']
            final = float(input) * float(euro)
            return render_template('index.html', moeda=f'US${final:.2f}')

        if value == 'iene' and value2 == 'yuan':
            return render_template('index.html', moeda='Operação indisponível no momento.')

        if value == 'iene' and value2 == 'real':
            real = get_coin('JPY', 'BRL', 'JPY', 'high')
            input = request.form['valor']
            final = float(input) * float(real)
            return render_template('index.html', moeda=f'R${final:.3f}')

        if value == 'yuan' and value2 == 'dolar-americano':
            dolar_americano = get_coin('CNY', 'USD', 'CNY', 'high')
            input = request.form['valor']
            final = float(input) * float(dolar_americano)
            return render_template('index.html', moeda=f'US${final:.2f}')

        if value == 'yuan' and value2 == 'dolar-canadense':
            return render_template('index.html', moeda=f'Operação indisponível no momento.')

        if value == 'yuan' and value2 == 'euro':
            euro = get_coin('CNY', 'EUR', 'CNY', 'high')
            input = request.form['valor']
            final = float(input) * float(euro)
            return render_template('index.html', moeda=f'€{final:.2f}')

        if value == 'yuan' and value2 == 'iene':
            return render_template('index.html', moeda=f'Operação indisponível no momento.')

        if value == 'yuan' and value2 == 'real':
            real = get_coin('CNY', 'BRL', 'CNY', 'high')
            input = request.form['valor']
            final = float(input) * float(real)
            return render_template('index.html', moeda=f'R${final:.2f}')

        if value == 'dolar-canadense' and value2 == 'real':
            real = get_coin('CAD', 'BRL', 'CAD', 'high')
            input = request.form['valor']
            final = float(input) * float(real)
            return render_template('index.html', moeda=f'R${final:.2f}')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
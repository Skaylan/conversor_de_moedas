from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_coin(moeda1, moeda2, value1, value2):
    url = requests.get(f'https://economia.awesomeapi.com.br/all/{moeda1}-{moeda2}')
    info = url.json()
    final_info = float(info[value1][value2])
    f_coin = float(final_info)
    return f_coin


def make_conversion(m1, m2, v1, v2):
        coin = get_coin(m1, m2, v1, v2)
        input = request.form['valor']
        final = float(input) * float(coin)
        return final

        





def make_conversion_division(m1, m2, v1, v2):
        coin = get_coin(m1, m2, v1, v2)
        input = request.form['valor']
        final = float(input) / float(coin)
        return final



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        value = request.form['moeda']
        value2 = request.form['moeda2']
        if value == 'real' and value2 == 'dolar-americano':
            moeda = make_conversion_division('USD', 'BRL', 'USD', 'high')
            return render_template('index.html', moeda=f'US${moeda:.2f}')

        if value == 'real' and value2 == 'dolar-canadense':
            moeda = make_conversion_division('CAD', 'BRL', 'CAD', 'high')
            return render_template('index.html', moeda=f'CAD${moeda:.2f}')

        if value == 'real' and value2 == 'euro':
            moeda = make_conversion_division('EUR', 'BRL', 'EUR', 'high')
            return render_template('index.html', moeda=f'€{moeda:.2f}')

        if value == 'real' and value2 == 'iene':
            moeda = make_conversion_division('JPY', 'BRL', 'JPY', 'high')
            return render_template('index.html', moeda=f'¥{moeda:.2f}')

        if value == 'real' and value2 == 'yuan':
            moeda = make_conversion_division('CNY', 'BRL', 'CNY', 'high')
            return render_template('index.html', moeda=f'CN¥{moeda:.2f}')

        if value == 'dolar-americano' and value2 == 'real':
            moeda = make_conversion('USD', 'BRL', 'USD', 'high')
            return render_template('index.html', moeda=f'R${moeda:.2f}')

        if value == 'dolar-americano' and value2 == 'dolar-canadense':
            moeda = make_conversion_division('CAD', 'USD', 'CAD', 'high')
            return render_template('index.html', moeda=f'CAD${moeda:.2f}')

        if value == 'dolar-americano' and value2 == 'euro':
            moeda = make_conversion_division('EUR', 'USD', 'EUR', 'high')
            return render_template('index.html', moeda=f'€{moeda:.2f}')

        if value == 'dolar-americano' and value2 == 'iene':
            moeda = make_conversion_division('JPY', 'USD', 'JPY', 'high')
            return render_template('index.html', moeda=f'¥{moeda * 100:.2f}')

        if value == 'dolar-americano' and value2 == 'yuan':
            moeda = make_conversion_division('CNY', 'USD', 'CNY', 'high')
            return render_template('index.html', moeda=f'CN¥{moeda:.2f}')

        if value == 'dolar-canadense' and value2 == 'real':
            moeda = make_conversion('CAD', 'BRL', 'CAD', 'high')
            return render_template('index.html', moeda=f'R${moeda:.2f}')

        if value == 'dolar-canadense' and value2 == 'dolar-americano':
            moeda = make_conversion('CAD', 'USD', 'CAD', 'high')
            return render_template('index.html', moeda=f'CAD${moeda:.2f}')

        if value == 'dolar-canadense' and value2 == 'euro':
            moeda = make_conversion('CAD', 'EUR', 'CAD', 'high')
            return render_template('index.html', moeda=f'€{moeda:.2f}')

        if value == 'dolar-canadense' and value2 == 'iene':
            return render_template('index.html', moeda=f'Operação indisponível no momento.')

        if value == 'dolar-canadense' and value2 == 'yuan':
            return render_template('index.html', moeda=f'Operação indisponível no momento.')

        if value == 'euro' and value2 == 'real':
            moeda = make_conversion('BRL', 'EUR', 'BRL', 'high')
            return render_template('index.html', moeda=f'R${moeda:.2f}')

        if value == 'euro' and value2 == 'dolar-americano':
            moeda = make_conversion('EUR', 'USD', 'EUR', 'high')
            return render_template('index.html', moeda=f'US${moeda:.2f}')

        if value == 'euro' and value2 == 'dolar-canadense':
            moeda = make_conversion('CAD', 'EUR', 'CAD', 'high')
            return render_template('index.html', moeda=f'CAD${moeda:.2f}')

        if value == 'euro' and value2 == 'iene':
            moeda = make_conversion_division('JPY', 'EUR', 'JPY', 'high')
            return render_template('index.html', moeda=f'¥{moeda * 100:.2f}')

        if value == 'euro' and value2 == 'yuan':
            moeda = make_conversion_division('CNY', 'EUR', 'CNY', 'high')
            return render_template('index.html', moeda=f'CN¥{moeda:.2f}')

        if value == 'iene' and value2 == 'real':
            moeda = make_conversion('JPY', 'BRL', 'JPY', 'high')
            return render_template('index.html', moeda=f'R${moeda:.2f}')

        if value == 'iene' and value2 == 'dolar-americano':
            return render_template('index.html', moeda=f'Operação indisponível no momento.')

        if value == 'iene' and value2 == 'dolar-canadense':
            return render_template('index.html', moeda=f'Operação indisponível no momento.')

        if value == 'iene' and value2 == 'euro':
            moeda = make_conversion('JPY', 'BRL', 'JPY', 'high')
            return render_template('index.html', moeda=f'€{moeda:.2f}')

        if value == 'iene' and value2 == 'yuan':
            moeda = make_conversion('JPY', 'BRL', 'JPY', 'high')
            return render_template('index.html', moeda=f'CN¥{moeda:.2f}')

        if value == 'yuan' and value2 == 'real':
            moeda = make_conversion('CNY', 'BRL', 'CNY', 'high')
            return render_template('index.html', moeda=f'R${moeda:.2f}')

        if value == 'yuan' and value2 == 'dolar-americano':
            moeda = make_conversion('CNY', 'USD', 'CNY', 'high')
            return render_template('index.html', moeda=f'US${moeda:.2f}')

        if value == 'yuan' and value2 == 'dolar-canadense':
            return render_template('index.html', moeda=f'Operação indisponível no momento.')

        if value == 'yuan' and value2 == 'euro':
            moeda = make_conversion('CNY', 'EUR', 'CNY', 'high')
            return render_template('index.html', moeda=f'€{moeda:.2f}')

        if value == 'yuan' and value2 == 'iene':
            return render_template('index.html', moeda=f'Operação indisponível no momento.')
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

line = ['инженер-исследователь',
        'пилот',
        'строитель',
        'экзобиолог',
        'врач',
        'инженер по терраформированию',
        'климатолог',
        'специалист по радиационной защите',
        'астрогеолог',
        'гляциолог',
        'инженер по жизнеобеспечению',
        'метеоролог',
        'оператор марсохода',
        'киберинженер',
        'штурман',
        'пилот дронов']

@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    if list_type == 'ul' or list_type == 'ol':
        return render_template('list_prof.html', line=line, type=list_type)
    else:
        return render_template('list_prof.html', line=line, type='error')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

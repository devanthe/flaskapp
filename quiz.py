# -*- coding: utf-8 -*-
# quiz/quiz.py

from flask import request, redirect, url_for, flash, Flask, render_template

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))

# lista pytań
DANE = [{
    'pytanie': 'Stolica Hiszpani, to:',  # pytanie
    'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],  # możliwe odpowiedzi
    'odpok': 'Madryt'},  # poprawna odpowiedź
    {
        'pytanie': 'Objętość sześcianu o boku 6 cm, wynosi:',
        'odpowiedzi': ['36', '216', '18'],
        'odpok': '216'},
    {
        'pytanie': 'Symbol pierwiastka Helu, to:',
        'odpowiedzi': ['Fe', 'H', 'He'],
        'odpok': 'He'},
    {
        'pytanie': 'Minecraft wersja Alpha 1.2.1 wyszła:',
        'odpowiedzi': ['5 listopada 2010', '3 marca 2009', '12 września 2011'],
        'odpok': '5 listopada 2010'},
]


@app.route('/', methods=['GET', 'POST'])
def index():
    # return 'Cześć, tu Python!'
    return render_template('index.html', pytania=DANE)


@app.route('/wynik', methods=['GET', 'POST'])
def wynik():
    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form

        for pnr, odp in odpowiedzi.items():
            if odp == DANE[int(pnr)]['odpok']:
                punkty += 1

        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(punkty))
        return redirect(url_for('wynik'))

    # return 'Cześć, tu Python!'
    return render_template('wynik.html', pytania=DANE)


if __name__ == '__main__':
    app.run(debug=True)
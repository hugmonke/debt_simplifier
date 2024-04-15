from flask import Flask, render_template, request
from algorithm import Calculator
app = Flask(__name__)
lista = []
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/kalkulator/')
def my_link():
  print ('I got clicked!')

  return render_template('main.html')

  
@app.route('/add/', methods=['GET', 'POST'])
def add():
  print ('Working!')
  if request.method=='POST':
    print("POST!")
    name1 = request.form['name1']
    name2 = request.form['name2']
    number = request.form['number']
    
    lista.append([name1, name2, number])
    return render_template('main_dodano.html')
  else:
    return render_template('main.html')
  
@app.route('/calc/', methods=['GET', 'POST'])
def calc():
  kalkulator = Calculator(lista)
  results = kalkulator.return_result()
  return render_template('wynik.html', list=results)
  
if __name__ == '__main__':
  app.run(debug=True)

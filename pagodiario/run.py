from flask import Flask
from flask import render_template, request, redirect
from flask import g

#from config import DevelopmentConfig

#from models import db
from models import Registro

import forms, sqlite3

app = Flask(__name__)

DATABASE = '/data/registro_diario.db'

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		sb = g._database = sqlite3.connect(DATABASE)
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/registro', methods=["GET","POST"])
def registro():
	registroform = forms.RegistroForm(request.form)
	if request.method == 'POST':
		registroform.fecha.data
		registroform.base.data
		registroform.gastos.data
		registroform.compras.data
		registroform.dinero.data
		registroform.ventas.data
		ganancia = int(registroform.base.data) + int(registroform.ventas.data)
		gasto = int(registroform.gastos.data) + int(registroform.compras.data)
		gasto1 = int(registroform.dinero.data) - int(gasto)
		total_f = int(ganancia) - int(gasto1)
		registroform.total.data = total_f#int(registroform.base.data)+int(registroform.gastos.data)+int(registroform.compras.data)+int(registroform.dinero.data)+int(registroform.ventas.data)
	return render_template('registro_diario.html', form = registroform)
		

if __name__ == '__main__':
	app.run(debug=True)
	db.init_app(app)
	with app.app_context():
		db.create_all()


"""base = request.form.get("base")
	gastos = request.form.get("gastos")
	compras = request.form.get("compras")
	dinero = request.form.get("dinero")
	ventas = request.form.get("ventas")
	return "<h1>El resultado de la suma es {}</h1>".format(int(base)+int(gastos)+int(compras)+int(dinero)+int(ventas))"""



#datos : no usar comentario en las paginas de html porque va a salir un error
#werkzeug.routing.BuildError


#Para llamar otras paginas desde la base
#se escribe la funcion a la cual va asociada 
#la pagina web no es necesario usar xnombre.html
#sino nombre claro si asi esta declarada
#la funcion en run.py

#base,gastos,compras del dia, dinero en efectivo, ventas del dia, total caja

"""
@app.route("/suma",methods=["GET","POST"])
def sumar():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        return "<h1>El resultado de la suma es {}</h1>".format(str(int(num1)+int(num2)))
"""

#base = 125650 1
#gastos = 20350 2
#compras = 15600 2
#dinero = 35500 3
#ventas = 55000 1
#total = 180200
#1 = 180650
#2 = 35950
#3-450
#ganancia = registroform.base.data + registroform.ventas.data
#gasto = registroform.gastos.data + registroform.compras.data
#gasto1 = gasto - registroform.dinero.data
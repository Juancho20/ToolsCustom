from flask import Flask
from flask import render_template, request, redirect
#from flask import g

#from config import DevelopmentConfig

#from models import db
#from models import Registro

import forms, sqlite3,getpass

app = Flask(__name__)

username = getpass.getuser()

#conexion = sqlite3.connect('C:/Users/'+username+'/Desktop/pagodiario/data/registro_diario.db')


#conexion.execute('CREATE TABLE Registro(fecha DATE,base INTEGER,gastos INTEGER,compras INTEGER,dinero INTEGER,ventas INTEGER,total INTEGER)')
#conexion.close()

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/registro', methods=["GET","POST"])
def registro():
	registroform = forms.RegistroForm(request.form)
	if request.method == 'POST':
		conexion = sqlite3.connect('C:/Users/'+username+'/Desktop/pagodiario/data/registro_diario.db')
		sentencia = conexion.cursor()
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
		sentencia.execute("INSERT INTO Registro(fecha,base,gastos,compras,dinero,ventas,total) VALUES (?,?,?,?,?,?,?)",(registroform.fecha.data,registroform.base.data,registroform.gastos.data,registroform.compras.data,registroform.dinero.data,registroform.ventas.data,registroform.total.data))	
		conexion.commit()
		registroform.fecha.data = ""
		registroform.base.data = ""
		registroform.gastos.data = ""
		registroform.compras.data = ""
		registroform.dinero.data = ""
		registroform.ventas.data = ""
		registroform.total.data = ""
		conexion.close()
	
	conexion_listar = sqlite3.connect('C:/Users/'+username+'/Desktop/pagodiario/data/registro_diario.db')
	conexion_listar.row_factory = sqlite3.Row

	cursor_listar = conexion_listar.cursor()
	cursor_listar.execute("SELECT fecha,base,gastos,compras,dinero,ventas,total FROM Registro")
	rows = cursor_listar.fetchall();
	#conexion_listar.close()
	return render_template('registro_diario.html', form = registroform, rows = rows)

@app.route('/estadisticas', methods=["GET", "POST"])
def estadisticas():
	#meses = ['01':'Enero','02':'Febrero','03':'Marzo','04':'Abril','05':'Mayo','06':'Junio',
	#		'07':'Julio','08':'Agosto','09':'Septiembre','10':'Octubre','11':'Noviembre','12':'Diciembre']
	buscarform = forms.BuscarForm(request.form)
	if request.method == 'POST':
		buscarform.mes.data
	conexion_listar = sqlite3.connect('C:/Users/'+username+'/Desktop/pagodiario/data/registro_diario.db')
	conexion_listar.row_factory = sqlite3.Row
	cursor_listar = conexion_listar.cursor()
	cursor_listar.execute("SELECT * FROM Registro WHERE fecha LIKE '%"+buscarform.mes.data+"%'")
	row = cursor_listar.fetchall();
	return render_template('estadisticas.html', form = buscarform, row = row)
		

if __name__ == '__main__':
	app.run(debug=True)
	#db.init_app(app)
	#with app.app_context():
	#	db.create_all()


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



#Tengo que unir lo que hice en estadisticas junto con registro_diario ya que encontre la forma de adicionar 
#el pequeño buscador
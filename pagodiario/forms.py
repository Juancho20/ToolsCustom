from wtforms import Form
from wtforms import StringField
from wtforms.fields.html5 import DateField

class RegistroForm(Form):
	#base,gastos,compras del dia, dinero en efectivo, ventas del dia, total caja
	fecha = DateField('Fecha')
	base = StringField('Base')
	gastos = StringField('Gastos')
	compras = StringField('Compras')
	dinero = StringField('Dinero')
	ventas = StringField('Ventas')
	total = StringField('Total')
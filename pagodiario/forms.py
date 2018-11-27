from wtforms import Form
from wtforms import StringField, SelectField
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

class BuscarForm(Form):
	mes = SelectField('Mes', choices = [('01','Enero'),('02','Febrero'),('03','Marzo'),('04','Abril'),('05','Mayo'),('06','Junio'),('07','Julio'),('08','Agosto'),('09','Septiembre'),('10','Octubre'),('11','Noviembre'),('12','Diciembre')])
	#dia = SelectField('Dia', choices = [('01'),('02')])
	#m = SelectField('Mes', choices = [('enero', 'Enero'), ('febrero', 'Febrero'), ('marzo', 'Marzo'), ('abril','Abril'), ('mayo','Mayo'),('mayo','Mayo'),('mayo','Mayo'),('mayo','Mayo'),('septiembre','Septiembre'),('octubre','Octubre'),('noviembre','Noviembre'),('diciembre','Diciembre')])
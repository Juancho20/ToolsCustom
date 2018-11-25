from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Registro(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	fecha = db.Column(db.Date())
	base = db.Column(db.Integer())
	gastos = db.Column(db.Integer())
	compras = db.Column(db.Integer())
	dinero = db.Column(db.Integer())
	ventas = db.Column(db.Integer())
	total = db.Column(db.Integer())
import os
import sys
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
session_flask = session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from numpy import NaN
from io import BytesIO
import base64
from base64 import b64encode
from sqlalchemy import or_
import time
import pandas as pd
from sqlalchemy import desc
from sqlalchemy import and_
from form import EnterData, Inicio_de_Sesion

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'secretkey123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uozkgicswjewvc:52d290cbd35bebf2c13bfafa6af69228235f21c7c5c1347f8e0f4331a7f441ba@ec2-54-160-109-68.compute-1.amazonaws.com:5432/dapiefrth8pcaq'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:diez203040@localhost:5432/template2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app)

db = SQLAlchemy(app)


# ----------------- CREACION DE LAS TABLAS PARA ANILLOS, CADENAS, PULSERAS Y ARETES ----------------- #
# --------------------------------------------------------------------------------------------------- #
class Anillos(db.Model):

    """
    id = El codigo unico del producto
    nombre = El nombre del producto
    descripcion = La descripcion del producto, si este se encuentra el mal estado, o si tiene algun defecto
    material = El material del producto ya sea oro, plata, acero, enchape, etc.
    precio = El precio del producto
    codigo = El codigo del producto que se vinculara con la tabla de imagenes ---- 100 + id
    empresa = La empresa que vende el producto, ya sea entre Rachel o Fashion
    """

    __tablename__ = 'anillos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String())
    descripcion = db.Column(db.String())
    material = db.Column(db.String())
    precio = db.Column(db.Integer)
    codigo = db.Column(db.Integer)
    empresa = db.Column(db.String())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'material': self.material,
            'precio': self.precio,
            'codigo': self.codigo,
            'empresa': self.empresa

        }
        
class Cadenas(db.Model):

    """
    id = El codigo unico del producto
    nombre = El nombre del producto
    descripcion = La descripcion del producto, si este se encuentra el mal estado, o si tiene algun defecto
    material = El material del producto ya sea oro, plata, acero, enchape, etc.
    precio = El precio del producto
    codigo = El codigo del producto que se vinculara con la tabla de imagenes ---- 200 + id
    empresa = La empresa que vende el producto, ya sea entre Rachel o Fashion
    """

    __tablename__ = 'cadenas'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String())
    descripcion = db.Column(db.String())
    material = db.Column(db.String())
    precio = db.Column(db.Integer)
    codigo = db.Column(db.Integer)
    empresa = db.Column(db.String())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'material': self.material,
            'precio': self.precio,
            'codigo': self.codigo,
            'empresa': self.empresa
        }

class Pulseras(db.Model):

    """
    id = El codigo unico del producto
    nombre = El nombre del producto
    descripcion = La descripcion del producto, si este se encuentra el mal estado, o si tiene algun defecto
    material = El material del producto ya sea oro, plata, acero, enchape, etc.
    precio = El precio del producto
    codigo = El codigo del producto que se vinculara con la tabla de imagenes ---- 300 + id
    empresa = La empresa que vende el producto, ya sea entre Rachel o Fashion
    """

    __tablename__ = 'pulseras'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String())
    descripcion = db.Column(db.String())
    material = db.Column(db.String())
    precio = db.Column(db.Integer)
    codigo = db.Column(db.Integer)
    empresa = db.Column(db.String())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'material': self.material,
            'precio': self.precio,
            'codigo': self.codigo,
            'empresa': self.empresa
        }

class Aretes(db.Model):

    """
    id = El codigo unico del producto
    nombre = El nombre del producto
    descripcion = La descripcion del producto, si este se encuentra el mal estado, o si tiene algun defecto
    material = El material del producto ya sea oro, plata, acero, enchape, etc.
    precio = El precio del producto
    codigo = El codigo del producto que se vinculara con la tabla de imagenes ---- 400 + id
    empresa = La empresa que vende el producto, ya sea entre Rachel o Fashion
    """

    __tablename__ = 'aretes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String())
    descripcion = db.Column(db.String())
    material = db.Column(db.String())
    precio = db.Column(db.Integer)
    codigo = db.Column(db.Integer)
    empresa = db.Column(db.String())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'material': self.material,
            'precio': self.precio,
            'codigo': self.codigo,
            'empresa': self.empresa
        }

class Juegos_de_Joyeria(db.Model):

    """
    id = El codigo unico del producto
    nombre = El nombre del producto
    descripcion = La descripcion del producto, si este se encuentra el mal estado, o si tiene algun defecto
    material = El material del producto ya sea oro, plata, acero, enchape, etc.
    precio = El precio del producto
    codigo = El codigo del producto que se vinculara con la tabla de imagenes ---- 500 + id
    empresa = La empresa que vende el producto, ya sea entre Rachel o Fashion
    """

    __tablename__ = 'juegos_de_joyeria'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String())
    descripcion = db.Column(db.String())
    material = db.Column(db.String())
    precio = db.Column(db.Integer)
    codigo = db.Column(db.Integer)
    empresa = db.Column(db.String())

    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'material': self.material,
            'precio': self.precio,
            'codigo': self.codigo,
            'empresa': self.empresa
        }

class Imagenes(db.Model):

    """
    id = El codigo unico del producto
    nombre = El nombre del producto
    codigo = El codigo del producto
    imagen = La imagen del producto
    """

    __tablename__ = 'imagenes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String())
    codigo = db.Column(db.Integer)
    imagen = db.Column(db.LargeBinary())
    @property
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'codigo': self.codigo,
            'imagen': self.imagen
        }


with app.app_context():
    db.create_all()

session = db.session

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/index/rachel menu principal')
def rachel_menu_principal():
    return render_template('/menu_principal_rachel.html')

@app.route('/index/fashion menu principal')
def fashion_menu_principal():
    return render_template('/menu_principal_fashion.html')

@app.route('/index/<joyeria>/anillos', methods=['GET', 'POST'])
def anillos(joyeria):
    menu_principal = joyeria.lower() + '_menu_principal'
    form = EnterData()
    if request.method == 'POST':
        len_anillo = len(session.query(Anillos).all()) + 1
        codigo_anillo = '100' + str(len_anillo)
        
        new_anillo = Anillos(nombre=request.form['nombre'], 
                            descripcion=request.form['descripcion'], 
                            material=request.form['material'], 
                            precio=float(request.form['precio']), 
                            codigo=int(codigo_anillo), 
                            empresa=joyeria)

        new_imagen = Imagenes(nombre=request.form['nombre'], 
                            codigo=int(codigo_anillo), 
                            imagen=request.files['imagen'].read())
        session.add(new_imagen)
        session.commit()

        flash(request.form['nombre'] + ' agregado exitosamente')
        return redirect(url_for('anillos', joyeria=joyeria, menu_principal=menu_principal))
    else:
        return render_template('anillos.html', form=form, joyeria=joyeria, menu_principal=menu_principal)

@app.route('/index/<joyeria>/aretes', methods=['GET', 'POST'])
def aretes(joyeria):
    menu_principal = joyeria.lower() + '_menu_principal'
    form = EnterData()
    if request.method == 'POST':
        len_arete = len(session.query(Aretes).all()) + 1
        codigo_arete = '400' + str(len_arete)
        
        new_arete = Aretes(nombre=request.form['nombre'], 
                            descripcion=request.form['descripcion'], 
                            material=request.form['material'], 
                            precio=float(request.form['precio']), 
                            codigo=int(codigo_arete), 
                            empresa=joyeria)
        session.add(new_arete)
        session.commit()

        new_imagen = Imagenes(nombre=request.form['nombre'], 
                            codigo=int(codigo_arete), 
                            imagen=request.files['imagen'].read())
        session.add(new_imagen)
        session.commit()

        flash(request.form['nombre'] + ' agregado exitosamente')
        return redirect(url_for('aretes', joyeria=joyeria, menu_principal=menu_principal))
    else:
        return render_template('aretes.html', form=form, joyeria=joyeria, menu_principal=menu_principal)

@app.route('/index/<joyeria>/cadenas', methods=['GET', 'POST'])
def cadenas(joyeria):
    menu_principal = joyeria.lower() + '_menu_principal'
    form = EnterData()
    if request.method == 'POST':
        len_collar = len(session.query(Cadenas).all()) + 1
        codigo_collar = '200' + str(len_collar)
        
        new_collar = Cadenas(nombre=request.form['nombre'], 
                            descripcion=request.form['descripcion'], 
                            material=request.form['material'], 
                            precio=float(request.form['precio']), 
                            codigo=int(codigo_collar), 
                            empresa=joyeria)
        session.add(new_collar)
        session.commit()

        new_imagen = Imagenes(nombre=request.form['nombre'], 
                            codigo=int(codigo_collar), 
                            imagen=request.files['imagen'].read())
        session.add(new_imagen)
        session.commit()

        flash(request.form['nombre'] + ' agregado exitosamente')
        return redirect(url_for('cadenas', joyeria=joyeria, menu_principal=menu_principal))
    else:
        return render_template('cadenas.html', form=form, joyeria=joyeria, menu_principal=menu_principal)

@app.route('/index/<joyeria>/pulseras', methods=['GET', 'POST'])
def pulseras(joyeria):
    menu_principal = joyeria.lower() + '_menu_principal'
    form = EnterData()
    if request.method == 'POST':
        len_pulsera = len(session.query(Pulseras).all()) + 1
        codigo_pulsera = '300' + str(len_pulsera)
        
        new_pulsera = Pulseras(nombre=request.form['nombre'], 
                            descripcion=request.form['descripcion'], 
                            material=request.form['material'], 
                            precio=float(request.form['precio']), 
                            codigo=int(codigo_pulsera), 
                            empresa=joyeria)
        session.add(new_pulsera)
        session.commit()

        new_imagen = Imagenes(nombre=request.form['nombre'], 
                            codigo=int(codigo_pulsera), 
                            imagen=request.files['imagen'].read())
        session.add(new_imagen)
        session.commit()

        flash(request.form['nombre'] + ' agregado exitosamente')
        return redirect(url_for('pulseras', joyeria=joyeria, menu_principal=menu_principal))
    else:
        return render_template('pulseras.html', form=form, joyeria=joyeria, menu_principal=menu_principal)

@app.route('/index/<joyeria>/juegos_de_joyeria', methods=['GET', 'POST'])
def juegos_de_joyeria(joyeria):
    menu_principal = joyeria.lower() + '_menu_principal'
    form = EnterData()
    if request.method == 'POST':
        len_juego = len(session.query(Juegos_de_Joyeria).all()) + 1
        codigo_juego = '500' + str(len_juego)
        
        new_juego = Juegos_de_Joyeria(nombre=request.form['nombre'], 
                            descripcion=request.form['descripcion'], 
                            material=request.form['material'], 
                            precio=float(request.form['precio']), 
                            codigo=int(codigo_juego), 
                            empresa=joyeria)
        session.add(new_juego)
        session.commit()

        new_imagen = Imagenes(nombre=request.form['nombre'], 
                            codigo=int(codigo_juego), 
                            imagen=request.files['imagen'].read())
        session.add(new_imagen)
        session.commit()

        flash(request.form['nombre'] + ' agregado exitosamente')
        return redirect(url_for('juegos_de_joyeria', joyeria=joyeria, menu_principal=menu_principal))
    else:
        return render_template('juegos_de_joyeria.html', form=form, joyeria=joyeria, menu_principal=menu_principal)

@app.route('/index/Inicio_de_sesion', methods=['GET', 'POST'])
def Inicio_de_sesion():
    usuarios = ['Norma', 'Tj', 'Kevin']
    clave = 10203040
    form = Inicio_de_Sesion()
    if request.method == 'POST':
        if request.form['usuario'] in usuarios and int(request.form['clave']) == clave:
            return redirect(url_for('Proveedores'))
        else:
            flash('Su clave o usuario son incorrectos')
            return redirect(url_for('Inicio_de_sesion'))
    else:
        return render_template('Inicio.html', form=form)

@app.route('/index/Inicio_de_sesion/proveedores', methods=['GET', 'POST'])
def Proveedores():
    return render_template('proveedores.html')


@app.route('/index/Inicio_de_sesion/proveedores/<joyeria>/Anillos', methods=['GET', 'POST'])
def Anillos_productos(joyeria):
    anillos = Anillos.query.filter_by(empresa=joyeria).all()
    return render_template('productos.html', joyeria=joyeria, producto='Anillos', productos_lista = anillos)


@app.route('/index/Inicio_de_sesion/proveedores/<joyeria>/Aretes', methods=['GET', 'POST'])
def Aretes_productos(joyeria):
    aretes = Aretes.query.filter_by(empresa=joyeria).all()
    return render_template('productos.html', joyeria=joyeria, producto='Aretes', productos_lista=aretes)


@app.route('/index/Inicio_de_sesion/proveedores/<joyeria>/Collares', methods=['GET', 'POST'])
def Collares_productos(joyeria):
    collares = Cadenas.query.filter_by(empresa=joyeria).all()
    return render_template('productos.html', joyeria=joyeria, producto='Collares', productos_lista=collares)


@app.route('/index/Inicio_de_sesion/proveedores/<joyeria>/Juego_de_joyeria', methods=['GET', 'POST'])
def Juego_de_joyeria_productos(joyeria):
    juego = Juegos_de_Joyeria.query.filter_by(empresa=joyeria).all()
    return render_template('productos.html', joyeria=joyeria, producto='Juegos de Joyeria', productos_lista=juego)


@app.route('/index/Inicio_de_sesion/proveedores/<joyeria>/Pulseras', methods=['GET', 'POST'])
def Pulseras_productos(joyeria):
    pulseras = Pulseras.query.filter_by(empresa=joyeria).all()
    return render_template('productos.html', joyeria=joyeria, producto='Pulseras', productos_lista=pulseras)

if __name__ == '__main__':
    app.secret_key = 'secret_key10'
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
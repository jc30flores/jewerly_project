from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, SelectField, DateField, TextAreaField, SelectMultipleField, DecimalField
from wtforms.validators import InputRequired, Email, Length, AnyOf
from flask_wtf.file import FileAllowed, FileField


class EnterData(Form):
    nombre = StringField('Nombre del Producto', validators=[InputRequired(), Length(min=4, max=25)])
    descripcion = TextAreaField('Descripcion Opcional del producto')
    material = StringField('Material del Producto', validators=[InputRequired()])
    precio = DecimalField('Precio', validators=[InputRequired()])
    imagen = FileField('Agregar una foto del Producto', validators=[FileAllowed(['jpg', 'png'], 'Solo se permiten imagenes')])

class Inicio_de_Sesion(Form):
    usuario = StringField('Nombre de Usuario', validators=[InputRequired()])
    clave = PasswordField('Contraseña', validators=[InputRequired()])


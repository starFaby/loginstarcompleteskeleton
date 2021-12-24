from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

#---------------------------
#drop database flaskmysql
#create database flaskmysql
#---------------------------

#----------usuario----------
#--------------------------
class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(80), nullable=False)
    nombres = db.Column(db.String(80), nullable=False)
    apellidos = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(250), nullable=True)
    cellphone = db.Column(db.String(100), nullable=False)
    isadmin = db.Column(db.Boolean, default=False)
    avatar = db.Column(db.String(250), nullable=True)
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 

    def onGetSetPassword(self, password):
        self.password = generate_password_hash(password)

    def onGetCheckPassword(self, password):
        return check_password_hash(self.password, password)

    def __init__(self, cedula, nombres, apellidos, username, email, password, cellphone, isadmin, avatar, estado, createdat):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.username = username
        self.email = email
        self.password = password
        self.cellphone = cellphone
        self.isadmin = isadmin
        self.avatar = avatar
        self.estado = estado
        self.createdat = createdat

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','cedula', 'nombres', 'apellidos', 'username', 'email', 'password', 'cellphone', 'isadmin', 'avatar', 'estado', 'createdat')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

#---------------------------
#----------NotaVenta----------
#--------------------------

class NotaVenta(db.Model):
    __tablename__='notaventas'

    id = db.Column(db.Integer, primary_key=True)
    numNotaVenta = db.Column(db.String(80), nullable=False)
    subtotal = db.Column(db.Numeric(8,2))
    dto = db.Column(db.Numeric(8,2))
    iva = db.Column(db.Numeric(8,2))
    total = db.Column(db.Numeric(8,2))
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 
    userid = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'), nullable=False)
    user = db.relationship('User',backref=db.backref('notaventas',lazy=True))


    def __init__(self, numNotaVenta, subtotal, dto, iva, total, estado, createdat):
        self.numNotaVenta = numNotaVenta
        self.subtotal = subtotal
        self.dto = dto
        self.iva = iva
        self.total = total
        self.estado = estado
        self.createdat = createdat

class NotaVentaSchema(ma.Schema):
    class Meta:
        fields = ('id','numNotaVenta', 'subtotal', 'dto', 'iva', 'total', 'estado', 'createdat')

notaVentaSchema = NotaVentaSchema()
notaVentaSchema = NotaVentaSchema(many=True)


#---------------------------
#----------detalleVentas----------
#--------------------------
class Detalleventa(db.Model):
    __tablename__='detalleventas'

    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    precio = db.Column(db.Numeric(8,2))
    total = db.Column(db.Numeric(8,2))
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 
    notaventaid = db.Column(db.Integer, db.ForeignKey('notaventas.id',ondelete='CASCADE'), nullable=False)
    notaventa = db.relationship('NotaVenta',backref=db.backref('detalleventas',lazy=True))
    productoid = db.Column(db.Integer, db.ForeignKey('productos.id',ondelete='CASCADE'), nullable=False)
    producto = db.relationship('Producto',backref=db.backref('detalleventas',lazy=True))

    def __init__(self, cantidad, precio, total, estado, createdat):
        self.cantidad = cantidad
        self.precio = precio
        self.total = total
        self.estado = estado
        self.createdat = createdat

class DetalleVentaSchema(ma.Schema):
    class Meta:
        fields = ('id','cantidad', 'precio', 'total', 'estado', 'createdat')

detalleVentaSchema = DetalleVentaSchema()
detalleVentaSchema = DetalleVentaSchema(many=True)

#---------------------------
#----------Productos----------
#--------------------------
class Producto(db.Model):
    __tablename__='productos'

    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.String(80), nullable=False)
    precio = db.Column(db.Numeric(10,2))
    total = db.Column(db.Numeric(10,2))
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 
    categoriaid = db.Column(db.Integer, db.ForeignKey('categorias.id',ondelete='CASCADE'), nullable=False)
    categoria = db.relationship('Categoria',backref=db.backref('productos',lazy=True))

    def __init__(self, cantidad, precio, total, estado, createdat):
        self.cantidad = cantidad
        self.precio = precio
        self.total = total
        self.estado = estado
        self.createdat = createdat

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id','cantidad', 'precio', 'total', 'estado', 'createdat')

productoSchema = ProductoSchema()
productoSchema = ProductoSchema(many=True)

#---------------------------
#----------Categoria----------
#--------------------------
class Categoria(db.Model):
    __tablename__='categorias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    image = db.Column(db.String(250), nullable=False)
    estado = db.Column(db.String(1), nullable=True)
    createdat = db.Column(db.String(11), nullable=True) 


    def __init__(self, nombre, image, estado, createdat):
        self.nombre = nombre
        self.image = image
        self.estado = estado
        self.createdat = createdat

class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre', 'image', 'estado', 'createdat')

categoriaSchema = CategoriaSchema()
categoriaSchema = CategoriaSchema(many=True)
# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categorias(models.Model):
    categoriaid = models.AutoField(db_column='categoriaId', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'categorias'


class Clientes(models.Model):
    clienteid = models.AutoField(db_column='clienteId', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS')
    apellido = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS')
    telefono = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'clientes'


class Detalleproducto(models.Model):
    detalleproductoid = models.AutoField(db_column='detalleProductoId', primary_key=True)  # Field name made lowercase.
    proveedorid = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='proveedorId')  # Field name made lowercase.
    productoid = models.ForeignKey('Productos', models.DO_NOTHING, db_column='productoId')  # Field name made lowercase.
    preciocompra = models.FloatField(db_column='precioCompra', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField()
    fecharegistro = models.DateField(db_column='fechaRegistro', blank=True, null=True)  # Field name made lowercase.
    fechacaducidad = models.DateField(db_column='fechaCaducidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalleProducto'


class Detalleventa(models.Model):
    detalleventaid = models.AutoField(db_column='detalleVentaId', primary_key=True)  # Field name made lowercase.
    ventaid = models.ForeignKey('Ventas', models.DO_NOTHING, db_column='ventaId')  # Field name made lowercase.
    productoid = models.ForeignKey('Productos', models.DO_NOTHING, db_column='productoId')  # Field name made lowercase.
    catidad = models.IntegerField()
    precioventa = models.FloatField(db_column='precioVenta')  # Field name made lowercase.
    subtotal = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalleVenta'


class Facturas(models.Model):
    facturasid = models.AutoField(db_column='facturasId', primary_key=True)  # Field name made lowercase.
    ventaid = models.ForeignKey('Ventas', models.DO_NOTHING, db_column='ventaId')  # Field name made lowercase.
    fechahora = models.DateTimeField(db_column='fechaHora')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facturas'


class Productos(models.Model):
    productoid = models.AutoField(db_column='productoId', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=20, db_collation='Modern_Spanish_CI_AS')
    precioventa = models.FloatField(db_column='precioVenta')  # Field name made lowercase.
    stock = models.IntegerField()
    descripcion = models.CharField(max_length=100, db_collation='Modern_Spanish_CI_AS')
    categoriaid = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='categoriaId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    proveedorid = models.AutoField(db_column='proveedorId', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS')
    direccion = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS')
    telefono = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'proveedores'


class Roles(models.Model):
    rolid = models.AutoField(db_column='rolId', primary_key=True)  # Field name made lowercase.
    desripcion = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS')

    class Meta:
        managed = False
        db_table = 'roles'


class Usuarios(models.Model):
    usuarioid = models.AutoField(db_column='usuarioId', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS')
    apellido = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS')
    telefono = models.CharField(max_length=30, db_collation='Modern_Spanish_CI_AS')
    rolid = models.ForeignKey(Roles, models.DO_NOTHING, db_column='rolId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios'


class Ventas(models.Model):
    ventaid = models.AutoField(db_column='ventaId', primary_key=True)  # Field name made lowercase.
    clienteid = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='clienteId', blank=True, null=True)  # Field name made lowercase.
    usuarioid = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='usuarioId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ventas'
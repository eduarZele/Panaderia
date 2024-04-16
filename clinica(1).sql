create database panaderiaDB

use panaderiaDB

create table roles(
	rolId int primary key identity(1,1),
	desripcion varchar(30) not null,
)


create table usuarios(
	usuarioId int primary key identity(1,1),
	nombre varchar(30) not null,
	apellido varchar(30) not null,
	telefono varchar(30) not null,
	rolId int not null,
	foreign key (rolId) references roles(rolId),


)

create table clientes(
	clienteId int primary key identity(1,1),
	nombre varchar(30) not null,
	apellido varchar(30) not null,
	telefono varchar(30) not null,
)


create table ventas(
	ventaId int primary key identity(1,1),
	clienteId int,
	foreign key (clienteId) references clientes(clienteId),
	usuarioId int not null,
	foreign key (usuarioId) references usuarios(usuarioId),
)


create table categorias(
	categoriaId int primary key identity(1,1),
	nombre varchar(30) not null, 
)


create table proveedores(
	proveedorId int primary key identity(1,1),
	nombre varchar(30) not null,
	direccion varchar(30) not null,
	telefono varchar(30) not null,
)


create table productos(
	productoId int primary key identity(1,1),
	nombre varchar(20) not null,
	precioVenta float not null,
	stock int not null,
	descripcion varchar(100) not null,
	categoriaId int not null,
	foreign key (categoriaId)references categorias(categoriaId),
)


create table detalleProducto(
	detalleProductoId int primary key identity(1,1),
	proveedorId int not null,
	foreign key (proveedorId) references proveedores(proveedorId)
	productoId int not null,
	foreign key (productoId) references productos(productoId),
	precioCompra float,
	cantidad int not null,
	fechaRegistro date,
	fechaCaducidad date,
)


 
create table detalleVenta(
	detalleVentaId int primary key identity(1,1),
	ventaId int not null,
	foreign key (ventaId) references ventas(ventaId),
	productoId int not null,
	foreign key (productoId) references productos(productoId),
	catidad int not null,
	precioVenta float not null,
	subtotal float not null,
)


create table facturas(
	facturasId int primary key identity(1,1),
	ventaId int not null,
	foreign key (ventaId) references ventas(ventaId),
	fechaHora datetime not null, 
)

-- Insertar roles
INSERT INTO roles (desripcion) VALUES ('Administrador');
INSERT INTO roles (desripcion) VALUES ('Vendedor');
INSERT INTO roles (desripcion) VALUES ('Cliente');

-- Insertar usuarios
INSERT INTO usuarios (nombre, apellido, telefono, rolId) VALUES ('Jair', 'Hernandez', '57033327', 1);
INSERT INTO usuarios (nombre, apellido, telefono, rolId) VALUES ('Eduardo', 'Zeledon', '84578747', 2);
INSERT INTO usuarios (nombre, apellido, telefono, rolId) VALUES ('Jesus', 'Nose', '52435747', 2);

-- Insertar clientes
INSERT INTO clientes (nombre, apellido, telefono) VALUES ('Carlos', 'Martínez', '5551236');
INSERT INTO clientes (nombre, apellido, telefono) VALUES ('Ana', 'López', '5556541');

-- Insertar categorías
INSERT INTO categorias (nombre) VALUES ('Panes');
INSERT INTO categorias (nombre) VALUES ('Pasteles');
INSERT INTO categorias (nombre) VALUES ('Bebidas');
INSERT INTO categorias (nombre) VALUES ('Lacteos');

-- Insertar proveedores
INSERT INTO proveedores (nombre, direccion, telefono) VALUES ('El Carmen', 'Masatepe', '59887675');
INSERT INTO proveedores (nombre, direccion, telefono) VALUES ('Cocacola', 'Calle 123', '999888777');
INSERT INTO proveedores (nombre, direccion, telefono) VALUES ('Centrolac', 'Avenida XYZ', '111222333');

-- Insertar productos
INSERT INTO productos (nombre, precioVenta, stock, descripcion, categoriaId) VALUES ('Pico', 8, 100, 'asd', 1);
INSERT INTO productos (nombre, precioVenta, stock, descripcion, categoriaId) VALUES ('Quesadilla', 8, 100, 'asd', 1);
INSERT INTO productos (nombre, precioVenta, stock, descripcion, categoriaId) VALUES ('Pastel 1lb', 250, 10, 'asd', 2);
INSERT INTO productos (nombre, precioVenta, stock, descripcion, categoriaId) VALUES ('Coca-cola', 20, 50, 'asd', 3);
INSERT INTO productos (nombre, precioVenta, stock, descripcion, categoriaId) VALUES ('Leche 1L', 22, 30, 'asd', 4);

-- Insertar detalle de productos
INSERT INTO detalleProducto (proveedorId, productoId, precioCompra, cantidad, fechaRegistro, fechaCaducidad) VALUES (1, 1, null, 100, '2024-03-15', '2024-05-01');
INSERT INTO detalleProducto (proveedorId, productoId, precioCompra, cantidad, fechaRegistro, fechaCaducidad) VALUES (1, 2, null, 100, '2024-03-20', '2024-05-01');
INSERT INTO detalleProducto (proveedorId, productoId, precioCompra, cantidad, fechaRegistro, fechaCaducidad) VALUES (1, 3, null, 100, '2024-03-20', '2024-05-01');
INSERT INTO detalleProducto (proveedorId, productoId, precioCompra, cantidad, fechaRegistro, fechaCaducidad) VALUES (2, 4, 14, 100, '2024-03-20', '2024-08-10');
INSERT INTO detalleProducto (proveedorId, productoId, precioCompra, cantidad, fechaRegistro, fechaCaducidad) VALUES (3, 5, 15, 100, '2024-03-20', '2024-08-10');

-- Insertar ventas
INSERT INTO ventas (clienteId, usuarioId) VALUES (1, 1);
INSERT INTO ventas (clienteId, usuarioId) VALUES (2, 2);
INSERT INTO ventas (clienteId, usuarioId) VALUES (null, 2);
INSERT INTO ventas (clienteId, usuarioId) VALUES (1, 3);
INSERT INTO ventas (clienteId, usuarioId) VALUES (null, 3);
INSERT INTO ventas (clienteId, usuarioId) VALUES (null, 3);


-- Insertar detalle de ventas
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (1, 1, 2, 8, 16);
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (1, 2, 2, 8, 16);
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (1, 4, 1, 20, 20);
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (2, 2, 1, 8, 8);
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (2, 5, 1, 22, 22);
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (3, 1, 2, 8, 16);
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (3, 2, 1, 8, 8);
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (3, 4, 1, 20, 20);
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (4, 3, 2, 250, 500);
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (5, 2, 2, 8, 16);
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (5, 4, 1, 20, 20);
INSERT INTO detalleVenta (ventaId, productoId, catidad, precioVenta, subtotal) VALUES (6, 2, 10, 8, 80);

-- Insertar facturas
INSERT INTO facturas (ventaId, fechaHora) VALUES (1, GETDATE());
INSERT INTO facturas (ventaId, fechaHora) VALUES (2, GETDATE());
INSERT INTO facturas (ventaId, fechaHora) VALUES (3, GETDATE());
INSERT INTO facturas (ventaId, fechaHora) VALUES (4, GETDATE());
INSERT INTO facturas (ventaId, fechaHora) VALUES (5, GETDATE());
INSERT INTO facturas (ventaId, fechaHora) VALUES (6, GETDATE());

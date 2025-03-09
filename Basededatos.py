import sqlite3  # Importamos la librería SQLite3 para manejar la base de datos

# Función para conectar con la base de datos
# Si el archivo "farmacia.db" no existe, SQLite lo creará automáticamente
def conectar():
    return sqlite3.connect("farmacia.db")

# Función para crear las tablas necesarias en la base de datos
def crear_tablas():
    # Establecemos conexión con la base de datos
    conexion = conectar()
    cursor = conexion.cursor()  # Obtenemos un cursor para ejecutar comandos SQL

    # 📌 Tabla de usuarios
    # Esta tabla almacena la información de los usuarios del sistema (empleados o administradores).
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador único del usuario
                        nombre TEXT NOT NULL,  -- Nombre del usuario
                        correo TEXT UNIQUE NOT NULL,  -- Correo electrónico único
                        contraseña TEXT NOT NULL,  -- Contraseña del usuario
                        tipo_usuario TEXT NOT NULL  -- Tipo de usuario (ejemplo: "admin" o "empleado")
                    )''')

    # 📌 Tabla de productos
    # Contiene los productos que se venden en la farmacia.
    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                        id_producto INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador único del producto
                        nombre TEXT NOT NULL,  -- Nombre del producto
                        descripcion TEXT,  -- Breve descripción del producto (opcional)
                        precio REAL NOT NULL,  -- Precio unitario del producto
                        stock INTEGER NOT NULL  -- Cantidad disponible en el inventario
                    )''')

    # 📌 Tabla de ventas
    # Almacena cada venta realizada por los usuarios del sistema.
    cursor.execute('''CREATE TABLE IF NOT EXISTS ventas (
                        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador único de la venta
                        id_usuario INTEGER NOT NULL,  -- Usuario que realizó la venta (referencia a "usuarios")
                        fecha TEXT NOT NULL,  -- Fecha y hora en la que se realizó la venta
                        FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)  -- Relación con la tabla "usuarios"
                    )''')

    # 📌 Tabla de detalle de ventas
    # Almacena los productos que fueron vendidos en cada transacción.
    cursor.execute('''CREATE TABLE IF NOT EXISTS detalle_ventas (
                        id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador único del detalle
                        id_venta INTEGER NOT NULL,  -- Identificador de la venta (relacionado con "ventas")
                        id_producto INTEGER NOT NULL,  -- Producto vendido (relacionado con "productos")
                        cantidad INTEGER NOT NULL,  -- Cantidad de unidades vendidas
                        precio_unitario REAL NOT NULL,  -- Precio unitario en el momento de la venta
                        total REAL NOT NULL,  -- Precio total (cantidad * precio_unitario)
                        FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),  -- Relación con "ventas"
                        FOREIGN KEY (id_producto) REFERENCES productos(id_producto)  -- Relación con "productos"
                    )''')

    # Guardamos los cambios en la base de datos
    conexion.commit()
    # Cerramos la conexión para liberar recursos
    conexion.close()

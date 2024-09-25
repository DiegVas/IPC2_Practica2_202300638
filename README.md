# Práctica 2 - Gestión de Autos con Flask

Este proyecto es parte de la **Práctica #2** del curso **Introducción a la Programación y Computación 2** de la Universidad de San Carlos de Guatemala. La práctica consiste en desarrollar una aplicación web para la gestión de autos utilizando el framework **Flask**.

## Descripción del Proyecto

La aplicación permite a los empleados de la agencia de autos **Super Autos GT** realizar las siguientes acciones:

- **Iniciar sesión** con un usuario y contraseña predefinidos.
- **Registrar nuevos autos** en el sistema.
- **Visualizar un listado** de los autos registrados.
- **Eliminar autos** cuando sea necesario.
- **Manejo de errores**, como evitar la duplicación de placas y validar entradas.

### Funcionalidades Principales

1. **Inicio de sesión**:
   - Usuario: `empleado`
   - Contraseña: `$uper4utos#`
   - Si los datos de inicio de sesión son incorrectos, se redirige al usuario a la página de inicio.

2. **Registro de autos**:
   - Los empleados pueden registrar autos con los siguientes campos:
     - `Placa`: Identificador único del auto.
     - `brand`: Marca del auto.
     - `model`: Modelo específico.
     - `description`: Descripción breve del auto.
     - `unit_price`: Precio por unidad en quetzales.
     - `quantity`: Número de unidades disponibles.
     - `image`: URL de la imagen representativa del auto.

3. **Visualización de autos**:
   - Listado completo de todos los autos registrados en el sistema en la página Home.

4. **Eliminación de autos**:
   - Posibilidad de eliminar autos basándose en su placa.

### Rutas y Funciones Principales

- `/`: Página de inicio (index)
- `/login`: Maneja el inicio de sesión (POST)
- `/Home`: Muestra la lista de autos registrados
- `/delete/<string:Placa>`: Elimina un auto por su placa (POST)
- `/Add`: Página para añadir un nuevo auto
- `/added`: Procesa la adición de un nuevo auto (POST)

## Estructura del Proyecto

```
proyecto/
│
├── app.py
|
├── classes/
│   └── car.py
|
├── templates/
│   ├── index.html
│   ├── Home.html
│   └── Add.html
|
└── README.md
```

## Detalles de Implementación

### Clase Car (car.py)

```python
class Car:
    def __init__(self, Placa, brand, model, description, unit_price, quantity, image):
        self.Placa = Placa
        self.brand = brand
        self.model = model
        self.description = description
        self.unit_price = unit_price
        self.quantity = quantity
        self.image = image
```

### Aplicación Principal (app.py)

- Utiliza Flask para crear una aplicación web.
- Mantiene una lista `carsRegistered` para almacenar los objetos Car.
- Implementa rutas para manejar diferentes funcionalidades (login, añadir auto, eliminar auto, etc.).
- Utiliza `render_template` para mostrar las páginas HTML.
- Implementa comprobación de sesión para asegurar que solo usuarios autenticados puedan acceder a ciertas funcionalidades.

## Instalación y Uso

1. **Clonar el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_DIRECTORIO>
   ```
   
2. **Instalar las dependencias**:
   ```bash
   pip install Flask
   ```

3. **Ejecutar la aplicación**:
   ```bash
   python app.py
   ```

4. **Acceder a la aplicación**:
   Abrir un navegador y visitar `http://localhost:3000`

## Tecnologías Utilizadas

- Python 3.x
- Flask
- HTML


# 🧾 CRM-Evolve

**CRM-Evolve** es una aplicación de consola desarrollada en Python para la gestión básica de relaciones con clientes (CRM). Permite registrar usuarios, crear facturas asociadas, realizar búsquedas, consultar facturas y obtener un resumen financiero general por cliente.

## 🚀 Funcionalidades

- ✅ Registro de usuarios con validaciones
- 🔍 Búsqueda de usuarios por nombre o email
- 🧾 Creación de facturas con ID personalizado (`FAC001`, `FAC002`, etc.)
- 📋 Listado completo de usuarios registrados
- 📑 Visualización de todas las facturas de un usuario
- 📊 Resumen financiero por cliente (facturas totales, pagadas, pendientes)
- 💾 Persistencia de datos con SQLite

## 🛠️ Tecnologías

- Lenguaje: **Python 3**
- Base de datos: **SQLite 3**
- Estructura modular con archivos separados para lógica, datos y consola

## 🧪 Ejecución del programa

1. Clona el repositorio:

```bash
git clone https://github.com/alejandroparodcristian/CRM-Evolve.git
cd CRM-Evolve
```

2. Ejecuta el menú principal:

```bash
python -m bd.menuPrincipal
```

> 💡 Asegúrate de tener Python instalado y estar en la raíz del proyecto.

## 🧾 Ejemplo de uso

```text
=== SISTEMA CRM ===
1. Registrar nuevo usuario
2. Buscar usuario
3. Crear factura para usuario
4. Mostrar todos los usuarios
5. Mostrar facturas de un usuario
6. Resumen financiero por usuario
7. Salir
```

## 📁 Estructura del proyecto

```
bd/
├── baseDatos/
│   ├── crearTablas.py
│   ├── conexion.py
├── usuario.py
├── factura.py
├── insertar.py
├── buscar.py
├── crearFactura.py
├── menuPrincipal.py
```

## 👨‍💻 Autor

**Alejandro Parod Cristian**  
📧 (puedes añadir tu correo aquí si deseas)  
🔗 [https://github.com/alejandroparodcristian](https://github.com/alejandroparodcristian)

## 📝 Licencia

Este proyecto es académico y se desarrolla como práctica de Tipología de Datos. Libre para uso educativo.

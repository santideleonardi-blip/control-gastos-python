# 💰 Sistema de Control de Gastos Personales

Aplicación interactiva ejecutada a través de la terminal, diseñada para registrar ingresos y gastos de forma organizada. Este proyecto fue desarrollado de forma independiente durante mi formación en la **Tecnicatura Superior en Desarrollo de Software (ISPC)**.

## 🚀 Características Clave
- **Persistencia de Datos:** Los registros no se pierden al cerrar el programa; se almacenan automáticamente en un archivo local `datos_gastos.json`.
- **Blindaje de Entradas (Manejo de Excepciones):** El sistema implementa bloques `try/except` para evitar colapsos o cierres inesperados si el usuario introduce caracteres alfabéticos por error en campos numéricos.
- **Validación Lógica:** Bloqueo automático ante intentos de registrar gastos mayores al saldo disponible actual.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3
- **Módulos Nativos:** `json` (manejador de persistencia) y `os` (verificador del sistema de archivos)

## 💻 Cómo Ejecutar el Proyecto
1. Asegúrate de tener instalado Python en tu equipo.
2. Descarga el archivo `control_gastos.py`.
3. Ejecuta el archivo desde tu terminal con el siguiente comando:
   ```bash
   python control_gastos.py
   ```

# 📊 Dashboard Cripto con Auto‑Refresh y Neon DB  
Proyecto Django

Este repositorio contiene un proyecto Django diseñado para mostrar un **dashboard de criptomonedas** con actualización automática (*auto‑refresh*) y conexión a una base de datos **Neon PostgreSQL**. Incluye además una estructura modular con una aplicación adicional llamada `crypto_site`.

---

## 🚀 Características principales

- Dashboard en tiempo real para visualizar precios o métricas de criptomonedas  
- Auto‑refresh implementado con JavaScript  
- Backend en Django con estructura modular  
- Base de datos Neon PostgreSQL  
- Middleware personalizado  
- Frontend en HTML integrado en las apps del proyecto  

---

## 📁 Estructura del proyecto

Da/
├── crypto_site/        # App secundaria del proyecto
├── dashboard/          # Dashboard cripto con auto-refresh
├── manage.py           # Script principal de Django
├── requirements.txt    # Dependencias del proyecto
└── .gitignore


---

## 🛠️ Instalación y configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/iwanehu/Da
cd Da
```
2️⃣ Crear entorno virtua
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

4️⃣ Configurar variables de entorno
Crea un archivo .env en la raíz del proyecto:
```bash
SECRET_KEY=tu_clave_secreta
DATABASE_URL=postgresql://usuario:password@host.neon.tech/dbname
DEBUG=True
```
5️⃣ Migraciones

```bash
python manage.py migrate
```

6️⃣ Ejecutar servidor

```bash
python manage.py runserver
```

🔄 Auto‑Refresh del Dashboard

El dashboard incluye un mecanismo de actualización automática mediante JavaScript (setInterval) y endpoints JSON en Django para obtener datos actualizados.

🧩 Middleware personalizado

El proyecto incluye un middleware propio que se ejecuta en cada request para manejar lógica adicional.
🗄️ Base de datos: Neon PostgreSQL

El proyecto está configurado para usar Neon, una base de datos PostgreSQL moderna, rápida y con plan gratuito.
📦 Dependencias principales

Las dependencias completas están en requirements.txt, pero típicamente incluyen:

    Django

    psycopg2 / psycopg2‑binary

    python‑dotenv

    requests

🤝 Contribuciones

Las contribuciones son bienvenidas.
Puedes abrir un issue o enviar un pull request.

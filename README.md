# El Gran Chancho API

API desarrollada con FastAPI que proporciona un endpoint `/chancho` que devuelve el mensaje "running".

## Características

- ✅ Endpoint `/chancho` que devuelve `{"message": "running"}`
- ✅ Endpoint raíz `/` con mensaje de bienvenida
- ✅ Endpoint `/health` para verificación de salud
- ✅ Documentación automática en `/docs`
- ✅ Dockerizado y listo para producción

## Instalación y Uso

### Desarrollo Local

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor de desarrollo
python main.py
```

### Con Docker

```bash
# Construir imagen
docker build -t el-gran-chancho .

# Ejecutar contenedor
docker run -p 8000:8000 el-gran-chancho
```

## Endpoints

- `GET /` - Mensaje de bienvenida
- `GET /chancho` - Estado del chancho (running)
- `GET /health` - Verificación de salud
- `GET /docs` - Documentación interactiva de la API

## Tecnologías

- **FastAPI**: Framework web moderno y rápido
- **Uvicorn**: Servidor ASGI de alto rendimiento
- **Python 3.11**: Versión optimizada para producción
- **Docker**: Containerización para despliegue
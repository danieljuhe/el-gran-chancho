from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
from typing import Dict

app = FastAPI(
    title="El Gran Chancho API",
    description="API del Gran Chancho - Endpoint para verificar estado",
    version="1.0.0"
)

@app.get("/chancho")
async def chancho_endpoint() -> Dict[str, str]:
    """
    Endpoint principal del Gran Chancho.
    
    Returns:
        Dict[str, str]: Mensaje de estado del chancho
    """
    return {"message": "running"}

@app.get("/")
async def root() -> Dict[str, str]:
    """
    Endpoint raíz de la API.
    
    Returns:
        Dict[str, str]: Mensaje de bienvenida
    """
    return {"message": "¡Bienvenido al Gran Chancho API!"}

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    Endpoint de verificación de salud.
    
    Returns:
        Dict[str, str]: Estado de salud del servicio
    """
    return {"status": "healthy", "service": "el-gran-chancho"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME)

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "secret-key-123":
        raise HTTPException(status_code=401, detail="Invalid or missing API Key")
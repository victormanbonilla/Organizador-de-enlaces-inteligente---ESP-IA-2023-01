from fastapi import Header, HTTPException
from functools import wraps
from .redis_cache import check_token

        
def jwt_validation(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        
        token = kwargs['token']
        if check_token(token):
            raise HTTPException(status_code=401, detail="Access denied")
        else:
            return await func(*args, **kwargs)
    return wrapper
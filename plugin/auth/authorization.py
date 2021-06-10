from fastapi import Depends, HTTPException
from .routers import get_current_user

async def get_current_admin_user(current_user: get_current_user = Depends()):
    if not current_user.disabled:
        raise HTTPException(status_code=400, detail="Only Admin")
    return current_user

async def get_current_common_user(current_user: get_current_user = Depends()):
    if current_user.disabled:
        return current_user
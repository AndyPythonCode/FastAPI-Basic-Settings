from fastapi import FastAPI
from typing import List

def adding_every_routers(routers: List[str], app: FastAPI) -> None:
    for router in routers:
        app.include_router(router)
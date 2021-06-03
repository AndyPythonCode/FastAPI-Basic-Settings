# Validate everydata that get in.

from fastapi import APIRouter

router_example = APIRouter(
	prefix="/example",
	tags=["Example"]
)

@router_example.get("/")
def Home_Example(): 
	return {"Hello":"World"}
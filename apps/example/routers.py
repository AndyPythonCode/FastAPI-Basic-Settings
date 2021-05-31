# Validate everydata that get in.

from fastapi import APIRouter

router_note = APIRouter(
	prefix="/note",
	tags=["Note"]
)

@router_note.get("/")
def Home():
	return 'yes'
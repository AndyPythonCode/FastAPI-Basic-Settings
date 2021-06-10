# Create you own path.
from typing import Dict, List
from fastapi import APIRouter
from fastapi.param_functions import Depends
from .models import example
from database.db import database
from .schemas import SchemasExample, SchemasExampleUpdate
from plugin.db.dml import ViewSets
from plugin.auth.authorization import get_current_admin_user, get_current_common_user

router_example = APIRouter(
	prefix="/example",
	tags=["Example"]
)

ViewModel = ViewSets(example, database)

@router_example.get("/", response_model=List[SchemasExampleUpdate])
async def Example_Read(current_user: get_current_common_user = Depends()): 
	return await ViewModel.List_Objects()

@router_example.get("/get/{id}", response_model=SchemasExampleUpdate)
async def Example_Read_One(id: int, current_user: get_current_common_user = Depends()): 
	return await ViewModel.Get_Object(id)

@router_example.post("/create", response_model=SchemasExampleUpdate)
async def Example_Create(request: SchemasExample, current_user: get_current_common_user = Depends()):
	return await ViewModel.Create_Object(request)

@router_example.put('/update', response_model=SchemasExampleUpdate)
async def Example_Update(request: SchemasExampleUpdate, current_user: get_current_common_user = Depends()):
	return await ViewModel.Updated_Object(request.id, request)

@router_example.delete('/delete/{id}', response_model=Dict[str, str])
async def Example_Delete(id: int, current_user: get_current_admin_user = Depends()):
	return await ViewModel.Delete_Object(id)
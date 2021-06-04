# Create you own path.
from typing import Dict, List
from fastapi import APIRouter
from .models import example
from .schemas import SchemasExample, SchemasExampleUpdate
from database.db import database
from plugin.db.functions import ViewSets

router_example = APIRouter(
	prefix="/example",
	tags=["Example"]
)

ViewModel = ViewSets(example, database)

@router_example.get("/", response_model=List[SchemasExampleUpdate])
async def Example_Read(): 
	return await ViewModel.List_Objects()

@router_example.get("/get/{id}", response_model=SchemasExampleUpdate)
async def Example_Read_One(id: int): 
	return await ViewModel.Get_Object(id)

@router_example.post("/create", response_model=SchemasExampleUpdate)
async def Example_Create(request: SchemasExample):
	return await ViewModel.Create_Object(request)

@router_example.put('/update', response_model=SchemasExampleUpdate)
async def Example_Update(request: SchemasExampleUpdate):
	return await ViewModel.Updated_Object(request.id, request)

@router_example.delete('/delete/{id}', response_model=Dict[str, str])
async def Example_Delete(id: int):
	return await ViewModel.Delete_Object(id)
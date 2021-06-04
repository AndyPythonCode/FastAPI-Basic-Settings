# Validate everydata that get in.

from pydantic import BaseModel
from typing import Optional

class SchemasExample(BaseModel):
	text: str
	completed: Optional[bool] = None

class SchemasExampleUpdate(BaseModel):
	id: int
	text: Optional[str]
	completed: Optional[bool]
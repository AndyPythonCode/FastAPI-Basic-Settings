# Create you own path.

from pydantic import BaseModel
from typing import Optional

class SchemasExample(BaseModel):
	text: str
	completed: Optional[bool]

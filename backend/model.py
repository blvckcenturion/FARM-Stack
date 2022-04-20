from typing import Optional
from pydantic import BaseModel
import datetime


class Todo(BaseModel):
    title: str
    description: str
    completed: Optional[bool] = False

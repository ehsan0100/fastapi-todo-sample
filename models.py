from pydantic import BaseModel, Field
from typing import Optional

class TodoItem(BaseModel):
    title: str = Field(..., title="عنوان وظیفه", example="یادگیری FastAPI")
    description: Optional[str] = Field(None, title="توضیحات تکمیلی", example="ساخت یک نمونه‌کار عالی برای گیت‌هاب")
    completed: bool = Field(False, title="وضعیت انجام", example=False)

class TodoResponse(TodoItem):
    id: int = Field(..., title="شناسه یکتا", example=1)

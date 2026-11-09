from fastapi import FastAPI, HTTPException
from typing import List
from models import TodoItem, TodoResponse

app = FastAPI(
    title="Todo API نمونه‌کار",
    description="یک API ساده و مدرن با FastAPI برای مدیریت وظایف روزانه",
    version="1.0.0"
)

# پایگاه داده موقت در حافظه (برای سادگی نمونه‌کار)
fake_db = []
counter = 1

@app.get("/", summary="صفحه اصلی")
def read_root():
    return {"message": "به FastAPI Todo API خوش آمدید! برای مستندات به آدرس /docs مراجعه کنید."}

@app.get("/todos", response_model=List[TodoResponse], summary="دریافت لیست تمام وظایف")
def get_todos():
    return fake_db

@app.post("/todos", response_model=TodoResponse, status_code=201, summary="ایجاد وظیفه جدید")
def create_todo(item: TodoItem):
    global counter
    new_item = {"id": counter, **item.dict()}
    fake_db.append(new_item)
    counter += 1
    return new_item

@app.delete("/todos/{todo_id}", summary="حذف وظیفه")
def delete_todo(todo_id: int):
    for index, item in enumerate(fake_db):
        item_id = item.get("id") if isinstance(item, dict) else item.id
        if item_id == todo_id:
            fake_db.pop(index)
            return {"message": f"وظیفه با شناسه {todo_id} با موفقیت حذف شد."}
    raise HTTPException(status_code=404, detail="وظیفه مورد نظر یافت نشد.")

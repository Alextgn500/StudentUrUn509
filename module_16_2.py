from fastapi import FastAPI, Path
from typing import Annotated

# Создание приложения FastAPI
app = FastAPI()

# Маршрут к главной странице
@app.get("/module_16_2")
async def main_page():
    return {"message": "Главная страница"}

# Маршрут к странице администратора
@app.get("/user/admin")
async def admin_page():
    return {"message": "Вы вошли как администратор"}

# Маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}")
async def user_page(user_id: Annotated[int, Path(ge=1, le=100, description= "Enter User ID",
                                        examples="2")]):# По умолчанию id = 2
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут к страницам пользователей с параметрами в адресной строке
@app.get("/user/{username}/{age}")
async def user_info(username: Annotated[str, Path( min_length=5, max_length=20,
                                        description="Enter Username", examples="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples="24")]):

    return {
        "message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
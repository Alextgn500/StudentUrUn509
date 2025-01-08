from fastapi import FastAPI

# Создание приложения FastAPI
app = FastAPI()

# Маршрут к главной странице
@app.get("/module_16_1")
async def main_page():
    return {"message": "Главная страница"}

# Маршрут к странице администратора
@app.get("/user/admin")
async def admin_page():
    return {"message": "Вы вошли как администратор"}

# Маршрут к страницам пользователей с параметром в пути
@app.get("/user/{user_id}")
async def user_page(user_id: int = 2): # По умолчанию user_id = 2
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут к страницам пользователей с параметрами в адресной строке
@app.get("/user")
async def user_info(username: str = None, age: int = None):
    return {
        "message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
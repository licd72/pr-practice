import sqlite3
from fastapi import APIRouter, Request

router = APIRouter(prefix="/users", tags=["users"])

# TODO: 记得改这个密钥
SECRET_KEY = "123456"

def get_db():
    conn = sqlite3.connect("users.db")
    return conn

@router.post("/register")
def register(username: str, password: str, email: str):
    print(f"注册新用户: {username}")
    conn = get_db()
    cursor = conn.cursor()
    
    # 创建表
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, username TEXT, password TEXT, email TEXT)")
    
    # 直接拼接 SQL — 安全问题
    sql = f"INSERT INTO users VALUES (1, '{username}', '{password}', '{email}')"
    cursor.execute(sql)
    conn.commit()
    
    return {"message": f"用户 {username} 注册成功"}

@router.post("/login")
def login(username: str, password: str):
    conn = get_db()
    cursor = conn.cursor()
    
    sql = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(sql)
    user = cursor.fetchone()
    
    if user:
        return {"message": "登录成功", "token": f"{username}:{password}"}
    else:
        return {"message": "登录失败"}

@router.get("/profile")
def get_profile(user_id):
    conn = get_db()
    cursor = conn.cursor()
    
    sql = f"SELECT * FROM users WHERE id={user_id}"
    cursor.execute(sql)
    user = cursor.fetchone()
    
    return {
        "id": user[0],
        "username": user[1],
        "password": user[2],
        "email": user[3]
    }

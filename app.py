# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, DevOps World! Это мой второй пуск CI"

# Это нужно для локального запуска, но не для продакшена
# if __name__ == '__main__':
#     app.run(debug=True)
